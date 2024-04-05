from .models import Student
from .serilizers import StudentSerializer
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from rest_framework.generics import  RetrieveUpdateDestroyAPIView,RetrieveAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# class LCStudent(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class RUDStudent(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

#Concrete api view in this more than one operation can work together 
#This class retrives the list of the records
class ListCreateStudent(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#This retrives the list by id and update delete it.
class RetriveUpdateDeleteStudent(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
