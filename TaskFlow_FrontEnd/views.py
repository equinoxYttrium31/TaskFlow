from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from . import models
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Home view (doesn't need changes)
def home_view(request):
    template = "MainPage.html"
    context = {
        'message': 'Welcome to TaskFlow',
    }
    return render(request, template, context)

# Login view (no changes needed here)
def Login(request):
    template = "Login.html"
    return render(request, template)

# Sign up and Sign in view
def save_user(request):
    if request.method == 'POST':
        action = request.POST.get('action')  # Get the action (signup or signin)

        if action == 'signup':
            # Handle Sign-Up (User Creation)
            Username = request.POST.get('Username')
            Email = request.POST.get('Email')
            Password = request.POST.get('Password')
            confirm_password = request.POST.get('ConfirmPassword')
            Role = request.POST.get('Role')

            # Basic validation
            if not Username or not Email or not Password or not confirm_password or not Role:
                messages.error(request, "All fields are required!")
                return redirect('Login')  # Redirect back to the same page with error

            # Check if passwords match
            if Password != confirm_password:
                messages.error(request, "Passwords do not match!")
                return redirect('Login')

            # Check if username or email already exists
            if models.User.objects.filter(Username=Username).exists():
                messages.error(request, "Username already exists!")
                return redirect('Login')

            if models.User.objects.filter(Email=Email).exists():
                messages.error(request, "Email is already registered!")
                return redirect('Login')

            # Hash the password before saving
            hashed_password = make_password(Password)

            # Create and save the user instance to the User model
            user = models.User(Username=Username, Email=Email, Password=hashed_password, Role=Role)
            user.save()

            # Success message and redirect to login page
            messages.success(request, "User created successfully!")
            return redirect('Login')  # Redirect to login page

        elif action == 'signin':
            # Handle Sign-In (Authentication)
            username = request.POST.get('Username')
            password = request.POST.get('Password')

            # Basic validation
            if not username or not password:
                messages.error(request, "Both username and password are required!")
                return redirect('Login')

            try:
                user = models.User.objects.get(username=username)
                if check_password(password, user.password):
                    # Password is correct, log the user in (optional, you can use Django's login function here)
                    messages.success(request, "Logged in successfully!")
                    return redirect('home_view')  # Redirect to home page after successful login
                else:
                    messages.error(request, "Incorrect password.")
                    return redirect('Login')
            except models.User.DoesNotExist:
                messages.error(request, "User does not exist.")
                return redirect('Login')

    # If it's not a POST request, just render the login page
    return render(request, 'Login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.sessions.models import Session
from .models import User  # Import your custom User model

def login_view(request):
    if request.method == 'POST':
        # Get username and password from the form
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        # Basic validation
        if not username or not password:
            messages.error(request, "Both username and password are required!")
            return redirect('Login')  # Redirect back to the same page with error

        try:
            # Fetch the user from the database
            user = User.objects.get(Username=username)

            # Check if the password matches
            if check_password(password, user.Password):
                # Log the user in by creating a session
                request.session['user_id'] = user.UserID
                request.session['username'] = user.Username
                messages.success(request, "Logged in successfully!")
                return redirect('home_view')  # Redirect to the home page
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('Login')  # Redirect back to the login page
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return redirect('Login')  # Redirect back to the login page

    # If it's not a POST request, just render the login page
    return render(request, 'Login.html')

