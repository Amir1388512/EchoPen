from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('SignUp/', signup_view, name='SignUp'),
    path('SignIn/', signin_view, name='SignIn'),
    path('Dashboard/<slug:slug>', dashboard_view, name='Dashboard'),
]
