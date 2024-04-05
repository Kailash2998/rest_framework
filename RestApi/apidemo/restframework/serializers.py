from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=70)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=70)

#deserialization
def create(self,validated_data):
    return Student.objects.create(**validated_data)