from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from . import models
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from .models import User 

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

def save_user(request):
    signup_messages = []
    show_signup = False  # Default to show Sign In form

    if request.method == 'POST':
        action = request.POST.get('action')  # 'signup' or 'signin'

        if action == 'signup':
            # Handle Sign-Up
            Username = request.POST.get('Username')
            Email = request.POST.get('Email')
            Password = request.POST.get('Password')
            confirm_password = request.POST.get('ConfirmPassword')
            Role = request.POST.get('Role')

            # Basic validation
            if not Username or not Email or not Password or not confirm_password or not Role:
                signup_messages.append(("All fields are required!", "error"))
                show_signup = True
            elif Password != confirm_password:
                signup_messages.append(("Passwords do not match!", "error"))
                show_signup = True
            elif models.User.objects.filter(Username=Username).exists():
                signup_messages.append(("Username already exists!", "error"))
                show_signup = True
            elif models.User.objects.filter(Email=Email).exists():
                signup_messages.append(("Email is already registered!", "error"))
                show_signup = True
            else:
                # Save user
                hashed_password = make_password(Password)
                user = models.User(
                    Username=Username, Email=Email, Password=hashed_password, Role=Role
                )
                user.save()
                messages.success(request, "User created successfully!")
                return redirect('Login')

        elif action == 'signin':
            # Handle Sign-In (already handled in `login_view`)

            return login_view(request)

    return render(
        request,
        "Login.html",
        {"signup_messages": signup_messages, "show_signup": show_signup},
    )

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

