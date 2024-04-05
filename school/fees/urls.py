from django.urls import path
from fees import views
urlpatterns = [
    path('fees/',views.temp1),
    path('',views.index)
]