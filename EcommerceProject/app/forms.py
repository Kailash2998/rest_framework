from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Customer
class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class' :'form-control'}))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class' :'form-control'}))
    email = forms.CharField(required='True' ,widget=forms.EmailInput(attrs={'class' :'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control' }))
    password = forms.CharField(label=("password"),strip=False,widget=forms.PasswordInput
               (attrs={'autocomplete':'currrent password','autofocus':True ,'class':'form-control' }))

class CustomerPasswordChange(PasswordChangeForm):
    old_password = forms.CharField(label=("old password"),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'currrent password' ,'autofocus':True,'class':'form-control' }))
    new_password1 = forms.CharField(label=("new password"),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'currrent password' ,'autofocus':True,'class':'form-control' }))
    new_password2 = forms.CharField(label=("confirm new password"),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'currrent password' ,'autofocus':True,'class':'form-control' }))

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=("Email"),max_length=254,
                             widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class PasswordResetConfirmForm(SetPasswordForm):
     new_password1 = forms.CharField(label=("new password"),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'currrent password' ,'autofocus':True,'class':'form-control' }))
     new_password2 = forms.CharField(label=("confirm new password"),strip=False,widget=forms.PasswordInput
    (attrs={'autocomplete':'currrent password' ,'autofocus':True,'class':'form-control' }))

class CutomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['id','name','locality','city','state','zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                   'locality':forms.TextInput(attrs={'class':'form-control'}),
                   'city':forms.TextInput(attrs={'class':'form-control'}),
                   'state':forms.Select(attrs={'class':'form-control'}),
                   'zipcode':forms.NumberInput(attrs={'class':'form-control'})}
    
    
                   