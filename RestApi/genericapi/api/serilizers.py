from rest_framework import serializers
from .models import Student

#using model serializer
class StudentSerializer(serializers.ModelSerializer):
     class Meta:
         model = Student
         fields= ['name','roll','city']
    