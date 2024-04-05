from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def student_detail(request,pk):
    #complex data
    stu=Student.objects.get(id=pk)
    print(stu)
    #serialization
    serializer =StudentSerializers(stu)
    print(serializer)
    #render into json
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')

def student_list(request):
    #complex data
    stu=Student.objects.all()
    print(stu)
    #serialization
    serializer =StudentSerializers(stu,many=True)
    print(serializer)
    #render into json
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')