from django.urls import path
from .views import *
from django.views.static import serve


urlpatterns = [
    path('', home_view, name='home'),
    path('SignUp/', signup_view, name='SignUp'),
    path('SignIn/', signin_view, name='SignIn'),
    path('Dashboard/<slug:slug>', dashboard_view, name='Dashboard'),
    path('LogOut/<slug:slug>', logout_view, name='LogOut'),
    path('contact/', contact_view, name='contact'),
    path('createArticle/', create_article_view, name='createArticle'),
    path('Articles/', article_view, name='Articles'),
    path('DeleteArticle/<slug:slug>', delete_article_view, name='DeleteArticle'),
    path('EditArticle/<slug:slug>', edit_article_view, name='EditArticle'),
]
