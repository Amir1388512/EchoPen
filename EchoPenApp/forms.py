from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from .models import *
from django import forms


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ("Username", "Email")


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = User
        fields = ("Username", "Email")

# Contact Form
class ContactForm(forms.Form):
    msg = forms.CharField(max_length=600, min_length=30, widget=forms.Textarea)
    fullName = forms.CharField(min_length=6, max_length=30)
    email = forms.EmailField(min_length=10, max_length=30)


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "content")
