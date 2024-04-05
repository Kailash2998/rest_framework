from django.contrib import admin
from enroll.models import Student
# Register your models here.

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','age','grade','email')
    
#admin.site.register(Student,StudentAdmin)
