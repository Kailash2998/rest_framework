
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('regstudent/',views.student_api),
    path('regstudent/<int:pk>',views.student_api),
]
