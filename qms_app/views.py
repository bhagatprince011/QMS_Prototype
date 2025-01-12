# In your_app/views.py

import datetime
import io
import os
import re
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import requests
from qms_app.models import *
from django.views.decorators.csrf import csrf_exempt
from supabase import create_client
from django.conf import settings
from qms_app.supabase_storage import *
from django.contrib import messages





@login_required(login_url='login')
def home(request):
    # Role-based filtering
    rolevalue = request.session.get('role', '').lower()  # Convert role to lowercase
    user_roads = Roads.objects.none()  # Default to an empty QuerySet
    user = request.user

    # Fetch roads based on role
    if rolevalue == 'contractor':
        user_roads = Roads.objects.filter(contractor_id=request.user.id)
    elif rolevalue == 'engineer':
        user_roads = Roads.objects.filter(engineer_id=request.user.id)
    elif rolevalue == 'administrator':
        user_roads = Roads.objects.all()

    # Filters mapping
    filters = {
        'name__icontains': request.GET.get('road_name', '').strip(),
        'source__icontains': request.GET.get('source', '').strip(),
        'destination__icontains': request.GET.get('destination', '').strip(),
        'road_type__name__icontains': request.GET.get('road_type', '').strip(),
        'milestone__name__icontains': request.GET.get('milestone', '').strip(),
        'contractor__first_name__icontains': request.GET.get('contractor', '').split(' ')[0].strip(),
        'engineer__first_name__icontains': request.GET.get('engineer', '').split(' ')[0].strip(),
    }

    # Remove any filters with empty values
    filters = {key: value for key, value in filters.items() if value}

    # Apply filters to the queryset
    user_roads = user_roads.filter(**filters)

    context = {
        'role': rolevalue,
        'name': f"{request.user.first_name} {request.user.last_name}",
        'user_roads': user_roads,
    }
    return render(request, 'home.html', context)





@login_required(login_url='login')
def contractor(request, road_id):
    road = get_object_or_404(Roads, id=road_id)

    print(road)
    milestones = [
        {"id": 11, "name": "M1"},
        {"id": 10, "name": "M2"},
        {"id": 9, "name": "M3"},
        {"id": 8, "name": "M4"},
        {"id": 7, "name": "M5"},
        {"id": 6, "name": "M6"},
        {"id": 5, "name": "M7"},
        {"id": 4, "name": "M8"},
        {"id": 3, "name": "M9"},
        {"id": 2, "name": "M10"},
        {"id": 1, "name": "M11"},
    ]
   

    return render(request, 'contractorView.html', {'road': road, 'milestones': milestones})


def engineer(request, road_id):
    road = get_object_or_404(Roads, id=road_id)
    message = request.session.get('message', None)
    
    
    print(road)
    milestones = [
        {"id": 11, "name": "M1"},
        {"id": 10, "name": "M2"},
        {"id": 9, "name": "M3"},
        {"id": 8, "name": "M4"},
        {"id": 7, "name": "M5"},
        {"id": 6, "name": "M6"},
        {"id": 5, "name": "M7"},
        {"id": 4, "name": "M8"},
        {"id": 3, "name": "M9"},
        {"id": 2, "name": "M10"},
        {"id": 1, "name": "M11"},
    ]
    params = {
        'road': road,
        'milestones': milestones,
        'fileErrorMessage': message 
    }
    request.session['message'] = None
    return render(request, 'engineerView.html', params)

def administrator(request, road_id):
    road = get_object_or_404(Roads, id=road_id)
    print(road)
    milestones = [
        {"id": 11, "name": "M1"},
        {"id": 10, "name": "M2"},
        {"id": 9, "name": "M3"},
        {"id": 8, "name": "M4"},
        {"id": 7, "name": "M5"},
        {"id": 6, "name": "M6"},
        {"id": 5, "name": "M7"},
        {"id": 4, "name": "M8"},
        {"id": 3, "name": "M9"},
        {"id": 2, "name": "M10"},
        {"id": 1, "name": "M11"},
    ]

    return render(request, 'administratorView.html', {'road': road, 'milestones': milestones})



def download_sample(request):
    file_name = "Sample/Framework for QMS.pdf"  # File in your Supabase Storage

    # Initialize SupabaseStorage class
    storage = SupabaseStorage()

    # Get the file's public URL
    file_url = storage.get_file_url(file_name)

    if not file_url:
        raise Http404("File not found.")

    # Request the file from the public URL
    file_content = storage.client.storage.from_(storage.bucket_name).download(file_name)

    if not file_content:
        raise Http404("Error downloading the file.")

    # Create a file response for direct download
    response = FileResponse(io.BytesIO(file_content), as_attachment=True, filename=file_name)
    return response


def downloadEvidence(request, road_id):
    storage = SupabaseStorage()

    # Get evidence data for the given road_id
    evidenceData = UploadedEvidenceFile()
    evidenceData = UploadedEvidenceFile.objects.filter(road_id=road_id).last()

    if not evidenceData:
        # Return JSON response with error message
        return JsonResponse({'success': False, 'message': 'No evidence found.'})

    file_name = evidenceData.file_name
    try:
        # Request the file from the public URL
        file_content = storage.client.storage.from_(storage.bucket_name).download(file_name)

        if not file_content:
            return JsonResponse({'success': False, 'message': 'Error downloading the file.'})

        # Return the file as a response (using FileResponse for proper handling)
        response = FileResponse(io.BytesIO(file_content), as_attachment=True, filename=file_name)
        return response

    except Exception as e:
        # If an error occurs, return the exception message
        return JsonResponse({'success': False, 'message': str(e)})


@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        # Get the uploaded file
        uploaded_file = request.FILES['files']  # Use 'files' to match the form input name
        road_id = request.POST.get('road_id')
        road = get_object_or_404(Roads, id=road_id)

        # Get the original file name and extension
        original_file_name, file_extension = os.path.splitext(uploaded_file.name)

        # Generate a new file name with the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        
        new_file_name = f"{original_file_name}_{timestamp}{file_extension}"
        
        # Initialize Supabase storage client
        storage = SupabaseStorage()

        # Upload the file to Supabase storage
        response = storage.upload_file(uploaded_file, new_file_name)

        if response.get('error'):
            return JsonResponse({'success': False, 'message': 'Failed to upload file.'})

        # Save the file URL to the model
        uploaded_file_record = UploadedEvidenceFile(
            road_id=road,
            milestone_id=road.milestone.next_milestone,
            file_name = new_file_name
        )
        uploaded_file_record.save()
        road.isUploadedProof = True
        road.save()
        print(uploaded_file_record.file_name)
        # Return only success message, without the URL
        return JsonResponse({'success': True, 'message': 'File uploaded successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})

def sendRemarks(request):
    if request.method == 'POST':
        remarks = request.POST.get('remarks')
        road_id = request.POST.get('road_id')
        print(remarks)
        print('road id: ', road_id)
        try:
            road = get_object_or_404(Roads, id=road_id)
            road.engineerMessage = remarks
            road.save()
            return JsonResponse({'success': True, 'message': 'Remarks saved successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Please try again later!.'})


def approve(request):
    if request.method == 'POST':
        road_id = request.POST.get('road_id')
        
        print('road id: ', road_id)
        try:
            road = get_object_or_404(Roads, id=road_id)
            road.isUploadedProof = False
            road.engineerMessage = None
            road.milestone = road.milestone.next_milestone
            
            road.save()
            return JsonResponse({'success': True, 'message': 'Approved successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Please try again later!.'})

# def apply_filters(filter_type, search_value, user_roads):
    
#     if not filter_type or not search_value:
#         return user_roads  # No filtering if no valid parameters

#     search_value = search_value.strip()

#     if filter_type == 'Engineer':
#         first_name = search_value.split(' ')[0]  # Handle first name only
#         engineer = Users.objects.filter(first_name__iexact=first_name).first()
#         if engineer:
#             return user_roads.filter(engineer_id=engineer.id)
#     elif filter_type == 'Contractor':
#         first_name = search_value.split(' ')[0]  # Handle first name only
#         contractor = Users.objects.filter(first_name__iexact=first_name).first()
#         if contractor:
#             return user_roads.filter(contractor_id=contractor.id)
#     elif filter_type == 'Source':
#         return user_roads.filter(source__iexact=search_value)
#     elif filter_type == 'Destination':
#         return user_roads.filter(destination__iexact=search_value)

#     return user_roads.none()  # Return an empty queryset for unsupported filters




