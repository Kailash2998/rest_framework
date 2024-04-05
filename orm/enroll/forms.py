from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField(initial='soham',help_text='har har mahadev!!!')
    email=forms.EmailField()
    
