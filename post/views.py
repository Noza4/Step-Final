import urllib
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

from post.models import Job


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Please log in.")
            return redirect("register")

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name  # Store full name in first_name
        user.save()

        # Log in the user automatically after registration
        login(request, user)

        # Store user data in session (without password)
        request.session["name"] = name
        request.session["email"] = email

        # Success message
        messages.success(request, "Registration successful!")

        # Redirect to role selection page
        return redirect("role")

    return render(request, "index.html")


def role_page(request):
    if not request.user.is_authenticated:  # Ensure the user is logged in
        return redirect("login")  # Redirect to login page if not authenticated

    name = request.session.get("name", "Guest")
    email = request.session.get("email", "")

    # Get the role from session (set in previous step)
    role = request.session.get("role", "guest")

    context = {"name": name, "email": email, "role": role}

    # If the user is a job seeker, load job listings
    if role == "Job Seeker":
        jobs = Job.objects.all()
        context["jobs"] = jobs  # Pass jobs to the template

    return render(request, "role.html", context)


def dashboard(request):
    role = request.GET.get('role', 'Job Seeker')  # Get role from request (optional)
    jobs = Job.objects.all()  # Query all jobs from the database

    context = {
        'role': role,
        'jobs': jobs  # Pass jobs to template
    }
    return render(request, 'dashboard.html', context)