"""
URL configuration for modelviewset project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

#The django provides the default router which has the all the root urls in application
router = DefaultRouter()
#studentapi = It is the api endpoint after application is run need to put that as suffix of url in browser.
#here router is register .StudentModelViewSet is the name of the class
router.register('studentapi',views.StudentModelViewSet,basename='student')


#urlpatterns are used to fire the api endpoint
#router.urls used to invoked the apis written ith the views.py and default router automatically taken those while we fires those api's.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
