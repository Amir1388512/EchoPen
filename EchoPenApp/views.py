from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

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
# ------------------------------------------------------------------
@login_required
def dashboard_view(request, slug):
    if slug is not None:
        username = slugify(request.user.Username)
        if username != slug:
            return redirect('home')
    return render(request, 'dashboard.html')
# ------------------------------------------------------------------


# Log Out 
# ------------------------------------------------------------------
@login_required
def logout_view(request, slug=None):
    if slug is not None:
        username = slugify(request.user.Username)
        if username != slug:
            return redirect('home')
    logout(request)
    return redirect('home')  # Redirect to login page after logout
# ------------------------------------------------------------------

# Contact 
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject='People Review',
                message= form.cleaned_data.get('msg'),
                from_email= form.cleaned_data.get('email'),
                recipient_list= ['amir.1388512.rezaie@gmail.com'],
                fail_silently=True,
            )
            return redirect('contact')
        else:
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html')