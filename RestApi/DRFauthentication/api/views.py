from .models import Student
from .serilizers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
#here this one class used to implement the all CRUD functionality . 
#ModelViewSet has the all built in functionalities of the CRUD operations.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=(BasicAuthentication,)
    #authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    
    #This line allow the all users to access the api.
    #permission_classes =[AllowAny]
    
    #This line allow to access the api only for those users whom staff status is checked.
    #permission_classes=[IsAdminUser]
    
    #The user is authenticated then it has all the permissions and if the user is not authenticated then the 
    #it readsonly
    #permission_classes = [IsAuthenticatedOrReadOnly]