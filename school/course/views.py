from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def temp2(request):
    context = {
        'name': 'John',
        'age': 30,
        'city': 'New York',
    }
    return render(request,'course/course.html',context)