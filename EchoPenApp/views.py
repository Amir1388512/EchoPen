from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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
    articles = Article.objects.all()
    articlesPublished = Article.published.all().count()
    articlesPending = Article.objects.filter(status="Pending").count()
    if slug is not None:
        username = slugify(request.user.Username)
        if username != slug:
            return redirect('home')
    return render(request, 'dashboard.html',
                  {"articles": articles, "articlesPublished": articlesPublished, 'articlesPending': articlesPending})


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
                message=form.cleaned_data.get('msg'),
                from_email=form.cleaned_data.get('email'),
                recipient_list=['amir.1388512.rezaie@gmail.com'],
                fail_silently=True,
            )
            return redirect('contact')
        else:
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


# CreateArticle
# ------------------------------------------------------------------
@login_required
def create_article_view(request):
    if request.method == "POST":
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = CreateArticleForm()
    return render(request, 'createArticle.html', {'form': form})


# ------------------------------------------------------------------


# Articles
# ------------------------------------------------------------------
def article_view(request):
    articlesPublished = Article.published.all()

    return render(request, 'articles.html', {'articles': articlesPublished})


# ------------------------------------------------------------------

# Delete Articles
# ------------------------------------------------------------------
@login_required
def delete_article_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author:
        return redirect('home')
    article.delete()
    return redirect('home')
# ------------------------------------------------------------------
