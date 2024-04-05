from django.shortcuts import render
from .forms import StudentRegistration
from .csrf_forms import CsrfForm
from .models import Student
# Create your views here.
def showformdata(request):
    fm=StudentRegistration()
    return render(request,'enroll/registration.html',{'form':fm})

def home(request):
    return render(request,'enroll/home.html')

def showcsrfformdata(request):
    if request.method == 'POST':
        frm=CsrfForm(request.POST)
        if frm.is_valid():
            print('user_name:',frm.cleaned_data['first_name'])
            print('user_email:',frm.cleaned_data['email'])
            ufm=frm.cleaned_data['first_name']
            ulm=frm.cleaned_data['last_name']
            ua=frm.cleaned_data['age']
            ug=frm.cleaned_data['grade']
            ue=frm.cleaned_data['email']
            # insert new records
            reg =Student(first_name=ufm, last_name=ulm, age=ua, grade=ug, email=ue)
            reg.save()
            #update existing record
            # reg =Student(id=1,first_name=ufm, last_name=ulm, age=ua, grade=ug, email=ue)
            # reg.save()
            #delete record
            # reg=Student(id=1)
            # reg.delete()
    else:
        frm=CsrfForm()
    return render(request,'enroll/csrf.html',{'form':frm})