from django.http import HttpResponse
from django.shortcuts import redirect, render

# In your_app/views.py
from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'Login.html'
    redirect_authenticated_user = True


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # Replace 'dashboard' with your desired URL name
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        if username == 'admin' and password == 'admin':
            request.session['authenticated'] = True
            return redirect('home')
        else:
             messages.error(request, "Invalid username or password")
    return render(request, 'Login.html')

def logout_page(request):
    #logout(request)  # Log out the user
    request.session['authenticated'] = False
    return redirect('login')  # Redirect to login page after logout
