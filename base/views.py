from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from os import path
from django.contrib.auth.decorators import login_required
from .models import Studenthome, Aprogrammes, Mentoring,SandPdetails,Attendance,Fstatement,PReport,dStudenthome, dAprogrammes, dMentoring,dSandPdetails,dAttendance,dFstatement,dPReport
from django.urls import reverse
from django.http import JsonResponse,HttpResponse
import requests
import json
import base64

# Create your views here.

def index(request):
	return render(request, 'base/index.html')


def charge(request):
	amount = 5
	if request.method == 'POST':
		print('Data:', request.POST)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})

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
            return redirect('shome')
        else:
            messages.info(request, 'Invalid Credentials ')
            return redirect('strathmorelogin')
            

    else:
        return render(request, 'base/strathmorelogin.html')


def daystar(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dhome')
        else:
            messages.info(request, 'Invalid Credentials ')
            return redirect('daystar')
            

    else:
        return render(request,'base/daystar.html')
@login_required(login_url='strathmorelogin')
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
    if request.method=='POST':
        phone=request.POST.get('pno')
        amount=request.POST.get('amount')
        urlname="http://127.0.0.1:8000/stkpush/"+phone+"/"+amount
        return redirect(urlname)
    return render(request,'base/spayfee.html')

def dsstudenthome(request):
    return render(request,'base/dsstudenthome.html')

def dfstructure(request):
    return render(request,'base/dfstructure.html')

def dattendance(request):
    user_object = User.objects.get(username=request.user.username)
    duser_attendance = dAttendance.objects.get(user=user_object) 
    return render(request,'base/dattendance.html',{'duser_attendance': duser_attendance})


def dfstatement(request):
    user_object = User.objects.get(username=request.user.username)
    duser_statement = dFstatement.objects.get(user=user_object) 
    return render(request,'base/dfstatement.html',{'duser_statement': duser_statement})


def dhome(request):
    user_object = User.objects.get(username=request.user.username)
    duser_profile = dStudenthome.objects.get(user=user_object) 
    duser_programmes = dAprogrammes.objects.get(user=user_object)
    duser_mentoring = dMentoring.objects.get(user=user_object) 


    return render(request,'base/dhome.html',{'duser_profile': duser_profile,'duser_programmes': duser_programmes,'duser_mentoring':duser_mentoring })
 

def dpfee(request):
    if request.method=='POST':
        phone=request.POST.get('pno')
        amount=request.POST.get('amount')
        urlname="http://127.0.0.1:8000/stkpush/"+phone+"/"+amount
        return redirect(urlname)
    return render(request,'base/dpfee.html')
    return render(request,'base/dpfee.html')

def dpreport(request):
    user_object = User.objects.get(username=request.user.username)
    duser_preport = dPReport.objects.get(user=user_object) 
    return render(request,'base/dpreport.html',{'duser_preport':duser_preport})
   
def dstudentdetails(request):
    user_object = User.objects.get(username=request.user.username)
    duser_details = dSandPdetails.objects.get(user=user_object) 
    return render(request,'base/dstudentdetails.html',{'duser_details': duser_details})
 

def deposit(request):
    return render(request,'base/deposit.html')

def stkpush(request,phone,cost):
    #Customer ID
    customer_key = "P5giKpFolWJzLQAqsLWYPJH7GWdS3X2A"
    # Customer secret
    customer_secret = "70otjSiYQptugMc6"
    # Concatenate customer key and customer secret and use base64 to encode the concatenated string
    credentials = customer_key + ":" + customer_secret
    # Encode with base64
    base64_credentials = base64.b64encode(credentials.encode("utf8"))
    credential = base64_credentials.decode("utf8")
    response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic '+credential })
    response=response.json()
    token=response['access_token']
    headers = {
    'Authorization': 'Bearer '+token,
     'Content-Type': 'application/json',
    }
    payload = {
        "BusinessShortCode": 174379,
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIwMzA3MTM1ODQy",
        "Timestamp": "20220307135842",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": cost,
        "PartyA": 254720163490,
        "PartyB": 174379,
        "PhoneNumber": phone,
        #change here
        "CallBackURL": "https://webhook.site/1b0e2900-564f-44f8-a23a-60e90f794c91",
        "AccountReference": "Pay Fee",
        "TransactionDesc": "Fee Payment" 
    }
    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json=payload)
    response=json.loads(response.text)
    return redirect(spayfee)