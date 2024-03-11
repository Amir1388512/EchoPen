from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


# Home View
# ------------------------------------------------------------------
def home_view(request):
    return render(request, 'home.html')

# ------------------------------------------------------------------


# Sign Up View
# ------------------------------------------------------------------
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('home')
        
# ------------------------------------------------------------------


# Sign in View 
# ------------------------------------------------------------------
def signin_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
    else:
        return redirect('home')
# ------------------------------------------------------------------


# Dashboard
def dashboard_view(request, slug):
    return HttpResponse(slug)