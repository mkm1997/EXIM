from django.forms import ModelForm
from django import forms
from .models import Student,Jobseeker,Company,College


class student(ModelForm):

    Password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        #add = Address.objects.filter(Student)
        model = Student
        fields = '__all__'
        #fields = 'add.__all__'

class jobseekers(ModelForm):

    Password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Jobseeker
        fields = '__all__'

class company(ModelForm):

    Password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Company
        fields = '__all__'

class college(ModelForm):


    Password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = College
        fields = '__all__'





