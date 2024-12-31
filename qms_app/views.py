# In your_app/views.py

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def home(request):
    # Check if the user is authenticated through session
    if not request.session.get('authenticated'):
        return redirect('login')  # Redirect to login if not authenticated
    return render(request, 'home.html')  # Render the home page

