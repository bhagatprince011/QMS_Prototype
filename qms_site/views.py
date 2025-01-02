# In your_app/views.py
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

class CustomLoginView(LoginView):
    template_name = 'Login.html'
    redirect_authenticated_user = True


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # Replace 'dashboard' with your desired URL name
    else:
        if request.method == 'POST':
            role = request.POST.get('role')
            username = request.POST.get('username')
            password = request.POST.get('password')
            #print(role)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['authenticated'] = True
                # Use reverse() and format the URL with the role parameter
                home_url = f"{reverse('home')}?role={role}"
                return redirect(home_url)
            else:
                messages.error(request, 'Invalid username or password.')
                    
        context = {}
        return render(request, 'Login.html', context)
    
    

def logout_page(request):
    logout(request)  # Log out the user
    request.session['authenticated'] = False
    return redirect('login')  # Redirect to login page after logout
