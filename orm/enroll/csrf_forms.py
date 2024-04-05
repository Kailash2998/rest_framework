from django import forms

class CsrfForm(forms.Form):
    first_name = forms.CharField(help_text='har har mahadev!!!')
    last_name = forms.CharField()
    age = forms.IntegerField()
    grade = forms.CharField()
    email = forms.EmailField()