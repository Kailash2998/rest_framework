from django.contrib import admin
from django.urls import path
from restframework import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studinfo/<int:pk>',views.student_detail),
    path('studinfo/',views.student_list),
]

