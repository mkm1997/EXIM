from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import FormView

from .forms import college,jobseekers,student,company
from django.contrib.auth.models import User
from .models import College,Company,Student,Jobseeker
from django.contrib.auth import authenticate, login, logout
from .models import Account

# Create your views here.

def home(request):
    if request.method == "POST":
        query = request.POST.get('search')


        if Company.objects.filter(email_id=query).exists():

            s=Company.objects.get(email_id=query)

            print(s)
            return render(request, 'info.html', {'Username': s.Username,
                  'Email': s.email,
                  'Phone_no.': s.ph_no,
                  'pincode': s.pincode,
                  'State': s.state,
                  'City': s.city,
                  'Country': s.Country
                  })

        elif Student.objects.filter(email=query).exists():

            s=Student.objects.get(email=query)
            #return render(request,'info.html',{'s':s})

            print(s)
            return render(request, 'info.html', {'Username':s.Username,
                'Email':s.email,
                'Phone_no.':s.Phone_no,
                'pincode':s.pincode,
                'State':s.state,
                'City':s.city,
                'Country':s.country
                })


        elif College.objects.filter(email_id=query).exists():

            s=College.objects.get(email_id=query)

            return render(request, 'info.html',{'Username': s.Username,
                  'Email': s.email,
                  'Phone_no.': s.ph_no,
                  'pincode': s.pincode,
                  'State': s.state,
                  'City': s.city,
                  'Country': s.Country
                  })

        
        elif Jobseeker.objects.filter(email1=query).exists():

            s=Jobseeker.objects.get(email1=query)

            return render(request, 'info.html', {'Username': s.Username,
                  'Email': s.email,
                  'Phone_no.': s.phone,
                  'pincode': s.pincode,
                  'State': s.state,
                  'City': s.city,
                  'Country': s.Country
                  })


        else:
            st="User Not Exist In Record"
            print(st)
            return render(request, 'info.html', {'st': st})



    return render(request,'home.html')

def search(request):
    if request.method=="POST":
        query=request.POST.get('search')

        if User.objects.filter(username=query).exists():
            print(query)





def index(request):

    if request.method == "POST":
        form = student(request.POST)
        if form.is_valid():

            username=request.POST.get('Username')
            password=request.POST.get('Password')
            print(username,password)

            user = User.objects.create_user(username=username, password=password)
            user.save()
            #acct = Account.objects.create(user=user)
            #acct.save()
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('Successfully Login')


        else:
            print(form.errors)
    else:
        form = student()


    return render(request,'student.html',{'form':form})

def Job(request):

    if request.method == "POST":
        form = jobseekers(request.POST)
        if form.is_valid():

            username=request.POST.get('Username')
            password=request.POST.get('Password')
            print(username,password)

            user = User.objects.create_user(username=username, password=password)
            user.save()
            #acct = Account.objects.create(user=user)
            #acct.save()
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('Successfully Login')


        else:
            print(form.errors)
    else:
        form = jobseekers()


    return render(request,'jobseekers.html',{'form':form})

def Compny(request):

    if request.method == "POST":
        form = company(request.POST)
        if form.is_valid():

            username=request.POST.get('Username')
            password=request.POST.get('Password')
            print(username,password)

            user = User.objects.create_user(username=username, password=password)
            user.save()
            #acct = Account.objects.create(user=user)
            #acct.save()
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('Successfully Login')



        else:
            print(form.errors)
    else:
        form = company()


    return render(request,'company.html',{'form':form})


def CLG(request):

    if request.method == "POST":
        form =  college(request.POST)
        if form.is_valid():

            username=request.POST.get('Username')
            password=request.POST.get('Password')
            print(username,password)

            user = User.objects.create_user(username=username, password=password)
            user.save()
            #acct = Account.objects.create(user=user)
            #acct.save()
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('Successfully Login')


        else:
            print(form.errors)
    else:
        form = college()


    return render(request,'college.html',{'form':form})




def LOGIN(request):
    #if request.user.is_authenticated():
        #return redirect('profile')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)  # going to login
                return HttpResponse("Loginsuccesfully")
            else:
                return HttpResponse("Account Not Active")
        else:
            print("SUMONE TRIED TO LOGIN AND FAILD")
            print("Username:{} and paswword {}".format(username, password))

        return HttpResponse("invalid login details suppiled")

    else:
        return render(request, 'Login.html', {})
