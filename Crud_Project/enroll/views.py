from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.
#Add data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            #fm.save()
            messages.add_message(request,messages.SUCCESS,'Your account has successfully been created !!!')
            fm=StudentRegistration()
    else:
        fm = StudentRegistration()
    stud=User.objects.all()
    return render(request,'enroll/addshow.html',{'form':fm,'stu':stud,})

#update and save record
def update_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/updateStudent.html',{'form':fm})

#delete record
def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')