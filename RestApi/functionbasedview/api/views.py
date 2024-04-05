from django.shortcuts import render
import io
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from .models import Student
from .serilizers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated,])

def student_api(request,pk=None):
    if request.method =='GET':
        #id=request.data.get('id')
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is created !!!'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
       # id = request.data.get('id')
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated!!!'})
        return Response(serializer.errors)
    
    if request.method =='DELETE':
        #id=request.data.get('id')
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Deleted Successfully!!!'})
        