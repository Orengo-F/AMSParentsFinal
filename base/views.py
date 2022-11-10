from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from os import path
from .models import Studenthome, Aprogrammes, Mentoring,SandPdetails,Attendance,Fstatement,PReport


# Create your views here.
def homepage(request):
    return render(request,'base/homepage.html')

def strathmore(request):
    return render(request,'base/strathmore.html')


def studentreg(request):
    if request.method== "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        myuser=User.objects.create_user(username, password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('strathmorelogin')
    return render(request,'base/studentreg.html')

def strathmorelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('strathmore')
        else:
            messages.info(request, 'Invalid Credentials ')
            return redirect('strathmorelogin')
            

    else:
        return render(request, 'base/strathmorelogin.html')


def daystar(request):
    return render(request,'base/daystar.html')

def shome(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Studenthome.objects.get(user=user_object) 
    user_programmes = Aprogrammes.objects.get(user=user_object)
    user_mentoring = Mentoring.objects.get(user=user_object) 


    return render(request,'base/shome.html',{'user_profile': user_profile,'user_programmes': user_programmes,'user_mentoring':user_mentoring })

def sstudentdetails(request):
    user_object = User.objects.get(username=request.user.username)
    user_details = SandPdetails.objects.get(user=user_object) 
    return render(request,'base/sstudentdetails.html',{'user_details': user_details})

def sattendance(request):
    user_object = User.objects.get(username=request.user.username)
    user_attendance = Attendance.objects.get(user=user_object) 
    return render(request,'base/sattendance.html',{'user_attendance': user_attendance})

def spreport(request):
    user_object = User.objects.get(username=request.user.username)
    user_preport = PReport.objects.get(user=user_object) 
    return render(request,'base/spreport.html',{'user_preport':user_preport})

def sfeestructure(request):
    return render(request,'base/sfeestructure.html')

def sfeestatement(request):
    user_object = User.objects.get(username=request.user.username)
    user_statement = Fstatement.objects.get(user=user_object) 
    return render(request,'base/sfeestatement.html',{'user_statement': user_statement})

def spayfee(request):
    return render(request,'base/spayfee.html')

def dsstudenthome(request):
    return render(request,'base/dsstudenthome.html')