from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def temp(request):
    return HttpResponse('<h1>temp page<h1>')
