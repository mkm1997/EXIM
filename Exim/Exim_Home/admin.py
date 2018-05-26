from django.contrib import admin
from .models import Student,Jobseeker,Company,College
# Register your models here.e
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Jobseeker)
admin.site.register(College)

