from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.showformdata),
    path('',views.home),
    path('csrf/',views.showcsrfformdata),
    path('csrf/',views.CsrfForm)
]