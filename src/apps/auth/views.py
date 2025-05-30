from django.shortcuts import render
from .forms import LoginForm, RegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login')  # change to your homepage url name
        messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('login')
        messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')
