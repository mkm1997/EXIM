from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)




Select_Category = (
    ('1','Scholarship'),
    ('2', 'Admission'),
    ('3','Part time job'),
    ('4','Campus job'),
    ('5','Internship'),
    ('6','Summer job'),
    ('7','Work From Home')

)


class Student(models.Model):


    #adderess = models.ForeignKey(Address,on_delete=models.CASCADE)
    Category = models.CharField(max_length=20,choices=Select_Category,default=1,blank=True,null=True)
    Username = models.CharField(max_length=20,primary_key=True)
    pincode = models.IntegerField()
    city = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    Qualifications = models.CharField(max_length=20,blank=True,null=True)
    Marks_percent = models.CharField(max_length=20,blank=True,null=True)
    Phone_no  = models.IntegerField(blank=True,null=True)
    Whatsapp_no = models.IntegerField(blank=True,null=True)
    email = models.EmailField()
    Linkdin_profile = models.URLField(blank=True,null=True)
    govt_id1=models.CharField(max_length=20,blank=True,null=True)
    govt_id2 = models.CharField(max_length=20,blank=True,null=True)
    D_O_B = models.DateField(blank=True,null=True)
    Home_pin = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.Username



Select_Ca = (
    ('1','Actively looking for job '),
    ('2', 'Service Notice period'),
    ('3','Looking for change'),
    ('4','Happy-but-want Onsite'),


)




class Jobseeker(models.Model):
    Status = models.CharField(max_length=20,choices=Select_Ca,blank=True,null=True)
    Username = models.CharField(max_length=20)

    pincode = models.IntegerField()
    city = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    #adderess = models.ForeignKey(Address, on_delete=models.CASCADE)
    Designation = models.CharField(max_length=20,blank=True,null=True)
    Skill = models.CharField(max_length=20,blank=True,null=True)
    Experience = models.CharField(max_length=100,blank=True,null=True)
    email1 = models.EmailField()
    Eemail2 = models.EmailField(blank=True,null=True)
    Phone = models.IntegerField(blank=True,null=True)
    Whatsapp_no = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.Username


Type_cmp = (
    ('1','Sole Properitership'),
    ('2', 'Partnership'),
    ('3','Pvt ltd'),

)

class Company(models.Model):
    Username = models.CharField(max_length=20)
    pincode = models.IntegerField()
    city = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    #adderess = models.ForeignKey(Address, on_delete=models.CASCADE)
    C_Reg_ID = models.CharField(max_length=40,blank=True,null=True)
    type_of_company = models.CharField(max_length=20,choices=Type_cmp,default=1,blank=True,null=True)
    email_id = models.EmailField()
    ph_no = models.IntegerField(blank=True,null=True)
    webLink = models.URLField(blank=True,null=True)
    Linkdine = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    fb = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.Username







class College(models.Model):
    Username = models.CharField(max_length=20)
    pincode = models.IntegerField()
    city = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    #adderess = models.ForeignKey(Address, on_delete=models.CASCADE)
    C_Reg_ID = models.CharField(max_length=40,blank=True,null=True)
    type_of_cmp = models.CharField(max_length=20,choices=Type_cmp,default=1,blank=True,null=True)
    email_id = models.EmailField()
    ph_no = models.IntegerField(blank=True,null=True)
    webLink = models.URLField(blank=True,null=True)
    Linkdine = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    fb = models.URLField(blank=True,null=True)
    def __str__(self):
        self.Username


