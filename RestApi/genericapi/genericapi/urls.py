
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('regstudent/',views.LCStudent.as_view()),
    path('regstudent/',views.ListCreateStudent.as_view()),
    #path('regstudent/<int:pk>',views.RUDStudent.as_view()),
    path('regstudent/<int:pk>',views.RetriveUpdateDeleteStudent.as_view()),
]
