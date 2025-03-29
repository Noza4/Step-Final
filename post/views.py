import urllib

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from post.models import Job
from post.serializers import JobSerializer


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


@login_required
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


@login_required
def dashboard(request):
    role = request.GET.get('role', '')

    if role == "Job_Seeker":
        # Show all available jobs
        jobs = Job.objects.all()
    elif role == "Employer":
        # Show only jobs posted by the logged-in employer
        jobs = Job.objects.filter(employer=request.user)
    else:
        # Redirect if role is not specified
        return redirect("role")

    context = {
        "role": role,
        "jobs": jobs
    }

    return render(request, "dashboard.html", context)


@api_view(['POST'])
def post_job(request):
    if request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new job
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'JobDetail.html', {'job': job})


def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  # Pass request here
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Set session data
            request.session["name"] = user.first_name
            request.session["email"] = user.email
            if "role" not in request.session:
                request.session["role"] = "Job Seeker"  # Default role

            messages.success(request, "Login successful!")
            return redirect("role")  # Make sure 'role' is defined in urls.py
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
