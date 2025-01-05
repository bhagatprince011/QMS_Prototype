# In your_app/views.py

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from qms_app.models import *
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



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
    if road.milestone == None:
        roadstart = True

    return render(request, 'contractorView.html', {'road': road, 'milestones': milestones, 'roadstart': roadstart})


@csrf_exempt
def upload_files(request):
    if request.method == "POST":
        uploaded_files = request.FILES.getlist('files')
        for file in uploaded_files:
            # Save file logic
            with open(f"uploads/{file.name}", 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        return JsonResponse({"message": "Files uploaded successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)

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