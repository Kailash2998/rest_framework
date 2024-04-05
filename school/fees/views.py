from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def temp1(request):
    return HttpResponse('<h1>Fees Page<h1>')
def index(request):
    return HttpResponse('<h1>Home Page<h1>')