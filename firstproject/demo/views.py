from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Home Page<h1>')

def learn_django(request):
    return HttpResponse('<h2>Hello Django<h2>')
