# In your_app/views.py

import io
import os
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from qms_app.models import *
from django.views.decorators.csrf import csrf_exempt
from supabase import create_client
from django.conf import settings
from qms_app.supabase_storage import *
from django.contrib import messages





@login_required(login_url='login')  # Ensures only authenticated users can access
def home(request):
    # Retrieve the role parameter from the query string
    role = request.GET.get('role')
    print('User role:', role)

    username = request.user.username
    name = request.user.first_name + ' ' + request.user.last_name

   # Determine roads based on the role
    if role == 'Contractor':
        user_roads = Roads.objects.filter(contractor_id=request.user.id)
    elif role == 'Engineer':
        user_roads = Roads.objects.filter(engineer_id=request.user.id)
    elif role == 'Administrator':
        user_roads = Roads.objects.all()
    else:
        user_roads = []  # Default to an empty list if the role is invalid or not provided

    # Prepare context for the template
    params = {
        'role': role,
        'name': name,
        'user_roads': user_roads,  # Pass the roads to the template
    }

    return render(request, 'home.html', params)


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

    return render(request, 'engineerView.html', {'road': road, 'milestones': milestones})

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

# # Handle file upload
# def upload_file(request):
#     if request.method == 'POST' and request.FILES.getlist('files'):
#         for file in request.FILES.getlist('files'):
#             UploadedFile.objects.create(file=file)
#         return redirect('contractor_view')  # Adjust to your contractor view URL name
#     return render(request, 'contractorView.html')

# # Handle file download
# def download_sample_file(request):
#     file_path = 'path/to/sample/file.pdf'  # Replace with your actual file path
#     return FileResponse(open(file_path, 'rb'), as_attachment=True)

# def get_public_url(bucket_name, file_name):
#     response = supabase.storage.from_(bucket_name).get_public_url(file_name)
#     if response.error:
#         raise Exception(f"Error generating public URL: {response.error.message}")
#     return response.public_url


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


@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        # Get the uploaded file
        uploaded_file = request.FILES['files']  # Use 'files' to match the form input name

        # Get the file name
        file_name = uploaded_file.name

        # Initialize Supabase storage client
        storage = SupabaseStorage()

        # Upload the file to Supabase storage
        response = storage.upload_file(uploaded_file, file_name)

        if response.get('error'):
            return JsonResponse({'success': False, 'message': 'Failed to upload file.'})
        else:
            return JsonResponse({'success': True, 'message': 'File uploaded successfully.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request.'})