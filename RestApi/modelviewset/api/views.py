from .models import Student
from .serilizers import StudentSerializer
from rest_framework import viewsets

#here this one class used to implement the all CRUD functionality . 
#ModelViewSet has the all built in functionalities of the CRUD operations.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
