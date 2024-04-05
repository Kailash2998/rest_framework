from rest_framework import serializers
from .models import Student

#using model serializer
class StudentSerializer(serializers.ModelSerializer):
     class Meta:
         model = Student
         fields= ['name','roll','city']
     
     #field validation in case of ModelSerializer 
     def validate_roll(self, value):
        """
        Validate the 'roll' field.
        """
        if value <= 0:
            raise serializers.ValidationError("Roll number must be a positive integer.")
        return value
    
    #object level validation in case of ModelSerializer
     def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('city must be ranchi')
        return data

#using normal serializer
# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=70)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=70)
    
#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         #this print the data present alredy in the db
#         print(instance.name)
#         instance.name=validated_data.get('name',instance.name)
#         #this is the data which will ready to update the existing data
#         print(instance.name)
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance
    
#     #field level validation
#     def validate_roll(self, value):
#         """
#         Validate the 'roll' field.
#         """
#         if value <= 0:
#             raise serializers.ValidationError("Roll number must be a positive integer.")
#         return value
    
#     #object level validation
#     def validate(self,data):
#         nm=data.get('name')
#         ct=data.get('city')
#         if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
#             raise serializers.ValidationError('city must be ranchi')
#         return data