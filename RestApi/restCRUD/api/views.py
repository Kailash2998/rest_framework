from django.shortcuts import render
import io
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from .models import Student
from .serilizers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
# Create your views here.
@api_view(['GET','POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method=='GET':
        #reads the json data from the request body
        json_data=request.body
        
        #then convert that into the byte stream beacuse the JSONParser().parse()crequired the data in byte stream
        #no in the string format
        stream=io.BytesIO(json_data)
        
        #it converts the byte stream data into the python data beacuse we need to work with the views functions 
        #django rest_framework compatible
        python_data=JSONParser().parse(stream)
        
        id=python_data.get('id',None)
        if id is not None:
            #it retrives the data from the db of pass unique id.
            stu=Student.objects.get(id=id)
            #serializer convert that python data into json data.
            serializer=StudentSerializer(stu)
            #then the JSONRenderer used to render the json data.
            json_data=JSONRenderer().render(serializer.data)
            #the the HttpResponse used to pass that json data to the end user or client which had fired the request.
            return HttpResponse(json_data,content_type='application/json')
        
        
        #it retrives the data for all the users.
        stu=Student.objects.all()
        #converts that python db data into the json data
        serializer=StudentSerializer(stu,many=True)
        #same as above it renders that json data
        json_data=JSONRenderer().render(serializer.data)
        #HttpResponse is created to pass the json_data to the end user
        return HttpResponse(json_data,content_type='application/json')
        
    #now work for to post the data
    if request.method =='POST':
        #this is the list,dictonary data
        json_data=request.body
        #convert into the byte stream
        stream=io.BytesIO(json_data)
        #convert into python data
        pythondata=JSONParser().parse(stream)
        #converts the python data to complext data and after that stored into the database.
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            #the respone is in the python dictonary format so need to convert into the json format
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        #if the data is not valid then it should gives the error
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    #now work for the update operation
    if request.method =='PUT':
        #this is the list,dictonary data
        json_data=request.body
        #convert into the byte stream
        stream=io.BytesIO(json_data)
        #convert into python data
        pythondata=JSONParser().parse(stream)
        #retrived the id
        id=pythondata.get('id')
        #get data for that id
        stu=Student.objects.get(id=id)
        #partial=True beacue we dont to updated complete data
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated!!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method =='DELETE':
         #this is the list,dictonary data
        json_data=request.body
        #convert into the byte stream
        stream=io.BytesIO(json_data)
        #convert into python data
        pythondata=JSONParser().parse(stream)
        #retrived the id
        id=pythondata.get('id')
        #get data for that id
        stu=Student.objects.get(id=id)
        #the function is deletes the record of unique id
        stu.delete()
        #the res is in the python dictonary format
        res={'msg':'Data Deleted!!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')   