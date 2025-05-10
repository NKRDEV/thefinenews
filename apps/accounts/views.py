from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            login(request, user)
            return redirect("home")  # Redirect to a home page or dashboard
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "accounts/profile.html")  # Render user profile page


@login_required
def edit_profile(request):
    # Logic for editing user profile goes here
    return render(request, "accounts/edit_profile.html")  # Render edit profile page


def login_view(request):
    return HttpResponse("Login Page")


def logout_view(request):
    return HttpResponse("Logout Page")


def register_view(request):
    return HttpResponse("Register Page")
