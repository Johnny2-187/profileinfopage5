from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    contact_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'username', 'contact_number', 'address', 'password')

class SignInForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'contact_number', 'address', 'username', 'password']