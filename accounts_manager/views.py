from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddPersonalInformationForm
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


def add_personal_information_view(request):
    context = {}
    context["form"] = AddPersonalInformationForm()
    return render(request, "addPersonalInfo.html", context)


def insert_personal_information(request):
    if request.method == "POST":
        username_input = request.POST.get("username")
        first_name_input = request.POST.get("first_name")
        last_name_input = request.POST.get("last_name")
        middle_name_input = request.POST.get("middle_name")
        email_input = request.POST.get("email")
        contact_number_input = request.POST.get("contact_number")
        address_input = request.POST.get("address")
        city_input = request.POST.get("city")
        zip_code_input = request.POST.get("zip_code")
        birthdate_input = request.POST.get("birthdate")
        
        # Instantiate Entity From KanjiQuiz Model
        personal_information_entity = PersonalInformation(
            username=username_input, last_name=last_name_input,
            first_name=first_name_input, middle_name=middle_name_input,
            email=email_input, contact_number=contact_number_input,
            address=address_input, city=city_input,
            zip_code=zip_code_input, birthdate=birthdate_input,
        )
        personal_information_entity.save()
        messages.success(request, "Personal Information Saved Successfully!")
        
        return redirect('add_personal_info')
    
    else:
        return redirect('add_personal_info')