from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import PersonalInformation


def home_view(request):
    # Check if user is logging in
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate User Login Request
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "You have been logged in")
            return redirect("home")
        else:
            messages.success(request, "Failed to login, Please try again")
            return redirect("home")
    else:
        records_list =  PersonalInformation.objects.values(
            "first_name", "last_name", "contact_number", 
            "email", "city", "birthdate", 
        )
        return render(request, "home.html", {"records": records_list})


def logout_user_view(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect("home")


def register_user_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Authenticate and Login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered!")
            return redirect("home")
    else:
        form = form = SignUpForm()
        return render(request, "register.html", {"form": form})
            
    return render(request, "register.html", {"form": form})


def profile_view(request):
    return render(request, "profile.html", {})
