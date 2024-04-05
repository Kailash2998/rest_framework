from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,UserProfileForm
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#Create your views here.
'''this states the used of the userreation form in the file which is predefined'''
# def signup(request):
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#            fm.save()
#     else:
#         fm=UserCreationForm()
#     return render(request,'enroll/signup.html',{'form':fm})

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
           fm.save()
           return HttpResponseRedirect("/login/")
    else:
        fm=SignupForm()
    return render(request,'enroll/signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fa = AuthenticationForm(request=request, data=request.POST)
            if fa.is_valid():
                uname = fa.cleaned_data['username']
                upass = fa.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,"successfully register!!!")
                    return HttpResponseRedirect('/profile/')
        else:
            fa = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form': fa})
    else:
        return HttpResponseRedirect('/profile/')
        
   

#profile page
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=UserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'profile updated successfully!!!')
                fm.save()
        else:
            fm=UserProfileForm(instance=request.user)
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
#function to logout user
def user_logout(request):
     logout(request)
     return HttpResponseRedirect('/login/')