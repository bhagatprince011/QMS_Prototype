from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class CustomLoginView(LoginView):
    template_name = 'Login.html'
    redirect_authenticated_user = True




def login_page(request):
    error_message = None
    if request.user.is_authenticated:
        return redirect('home')  # Redirect authenticated users to 'home'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'admin' and password == '123':
            return redirect('home')
        #user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('home')  # Replace 'home' with the URL name of your desired page
        else:
            # Add an error message
            messages.error(request, "Invalid username or password")

    return render(request, 'Login.html')
