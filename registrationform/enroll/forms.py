from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','id','first_name','last_name','email']
        labels={'email':'Email'}

class UserProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=['username','id','first_name','last_name','email','date_joined']
        labels={'email':'Email'}

