# In your_app/views.py

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from qms_app.models import *


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


