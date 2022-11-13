from email.policy import default
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser

User = get_user_model()

# Create your models here.
class Studenthome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    username = models.TextField(blank=True)
    email = models.TextField(blank=True)
    dob = models.TextField(blank=True)
    mno = models.IntegerField(blank=True)
    pschool = models.TextField(blank=True)
    religion = models.TextField(blank=True)
    def __str__(self):
        return self.user.username

class Aprogrammes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    programmme = models.TextField(blank=True)
    syllabus= models.TextField(blank=True)
    status= models.TextField(blank=True)
    intake = models.TextField(blank=True)
    def __str__(self):
        return self.user.username


class Mentoring(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    cmentor = models.TextField(blank=True)
    memail= models.TextField(blank=True)
    dls= models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class SandPdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    idno = models.IntegerField(blank=True)
    paddress= models.TextField(blank=True)
    town= models.TextField(blank=True)
    hcountry = models.TextField(blank=True)
    residence= models.TextField(blank=True)
    religion= models.TextField(blank=True)
    pcode = models.TextField(blank=True)
    mstatus= models.TextField(blank=True)
    mno= models.TextField(blank=True)
    pemail = models.TextField(blank=True)
    faname= models.TextField(blank=True)
    fmno= models.TextField(blank=True)
    femail = models.TextField(blank=True)
    foccup= models.TextField(blank=True)
    mname= models.TextField(blank=True)
    memail = models.TextField(blank=True)
    mmno= models.TextField(blank=True)
    moccup= models.TextField(blank=True)
    gname = models.TextField(blank=True)
    gmno= models.TextField(blank=True)
    gemail = models.TextField(blank=True)
    goccup = models.TextField(blank=True)


    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    unit1 = models.TextField(blank=True)
    unit2= models.TextField(blank=True)
    unit3= models.TextField(blank=True)
    unit4 = models.TextField(blank=True)
    unit5= models.TextField(blank=True)
    unit6= models.TextField(blank=True)
    unit7 = models.TextField(blank=True)
    att1= models.TextField(blank=True)
    att2= models.TextField(blank=True)
    att3 = models.TextField(blank=True)
    att4= models.TextField(blank=True)
    att5= models.TextField(blank=True)
    att6 = models.TextField(blank=True)
    att7= models.TextField(blank=True)


    def __str__(self):
        return self.user.username

class Fstatement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    date1 =  models.IntegerField(blank=True, null=True)
    date2 =  models.IntegerField(blank=True, null=True)
    date3 =  models.IntegerField(blank=True,null=True)
    date4 =  models.IntegerField(blank=True,null=True)
    date5 =  models.IntegerField(blank=True,null=True)
    date6 =  models.IntegerField(blank=True,null=True)
    date7 =  models.IntegerField(blank=True,null=True)
    date8 =  models.IntegerField(blank=True,null=True)
    date9 =  models.IntegerField(blank=True,null=True)
    date10 =  models.IntegerField(blank=True,null=True)
    date11 =  models.IntegerField(blank=True,null=True)
    dno1 =  models.IntegerField(blank=True,null=True)
    dno2 =  models.IntegerField(blank=True,null=True)
    dno3 =  models.IntegerField(blank=True,null=True)
    dno4 =  models.IntegerField(blank=True,null=True)
    dno5 =  models.IntegerField(blank=True,null=True)
    dno6 =  models.IntegerField(blank=True,null=True)
    dno7 =  models.IntegerField(blank=True,null=True)
    dno8 =  models.IntegerField(blank=True,null=True)
    dno9 =  models.IntegerField(blank=True,null=True)
    dno10 =  models.IntegerField(blank=True,null=True)
    dno11 =  models.IntegerField(blank=True,null=True)
    dtype1 = models.TextField(blank=True)
    dtype2= models.TextField(blank=True)
    dtype3= models.TextField(blank=True)
    dtype4= models.TextField(blank=True)
    dtype5= models.TextField(blank=True)
    dtype6= models.TextField(blank=True)
    dtype7 = models.TextField(blank=True)
    dtype8= models.TextField(blank=True)
    dtype9= models.TextField(blank=True)
    dtype10 = models.TextField(blank=True)
    dtype11= models.TextField(blank=True)
    debit1 =  models.IntegerField(blank=True,null=True)
    debit2 =  models.IntegerField(blank=True,null=True)
    debit3 =  models.IntegerField(blank=True,null=True)
    debit4 =  models.IntegerField(blank=True,null=True)
    debit5 =  models.IntegerField(blank=True,null=True)
    debit6 =  models.IntegerField(blank=True,null=True)
    debit7 =  models.IntegerField(blank=True,null=True)
    debit8 =  models.IntegerField(blank=True,null=True)
    debit9 =  models.IntegerField(blank=True,null=True)
    debit10 =  models.IntegerField(blank=True,null=True)
    debit11 =  models.IntegerField(blank=True,null=True)
    credit1 =  models.IntegerField(blank=True,null=True)
    credit2 =  models.IntegerField(blank=True,null=True)
    credit3 =  models.IntegerField(blank=True,null=True)
    credit4 =  models.IntegerField(blank=True,null=True)
    credit5 =  models.IntegerField(blank=True,null=True)
    credit6 =  models.IntegerField(blank=True,null=True)
    credit7 =  models.IntegerField(blank=True,null=True)
    credit8 =  models.IntegerField(blank=True,null=True)
    credit9 =  models.IntegerField(blank=True,null=True)
    credit10 =  models.IntegerField(blank=True,null=True)
    credit11 =  models.IntegerField(blank=True,null=True)
    totdeb =  models.IntegerField(blank=True,null=True)
    totcred =  models.IntegerField(blank=True,null=True)
  


    def __str__(self):
        return self.user.username

class PReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    unit1 = models.TextField(blank=True)
    unit2= models.TextField(blank=True)
    unit3= models.TextField(blank=True)
    unit4 = models.TextField(blank=True)
    unit5= models.TextField(blank=True)
    unit6= models.TextField(blank=True)
    unit7 = models.TextField(blank=True)
    unit8 = models.TextField(blank=True)
    unit9= models.TextField(blank=True)
    unit10= models.TextField(blank=True)
    unit11 = models.TextField(blank=True)
    unit12= models.TextField(blank=True)
    unit13= models.TextField(blank=True)
    unit14= models.TextField(blank=True)
    unit15= models.TextField(blank=True)
    unit16= models.TextField(blank=True)
    unit17= models.TextField(blank=True)
    unit18 = models.TextField(blank=True)
    unit19= models.TextField(blank=True)
    unit20= models.TextField(blank=True)
    unit21 = models.TextField(blank=True)
    att1= models.TextField(blank=True)
    att2= models.TextField(blank=True)
    att3 = models.TextField(blank=True)
    att4= models.TextField(blank=True)
    att5= models.TextField(blank=True)
    att6 = models.TextField(blank=True)
    att7= models.TextField(blank=True)
    att8= models.TextField(blank=True)
    att9= models.TextField(blank=True)
    att10 = models.TextField(blank=True)
    att11= models.TextField(blank=True)
    att12= models.TextField(blank=True)
    att13= models.TextField(blank=True)
    att14 = models.TextField(blank=True)
    att15= models.TextField(blank=True)
    att16= models.TextField(blank=True)
    att17 = models.TextField(blank=True)
    att18= models.TextField(blank=True)
    att19= models.TextField(blank=True)
    att20= models.TextField(blank=True)
    att21= models.TextField(blank=True)
    pend1=models.TextField(blank=True)
    pend2=models.TextField(blank=True)
    pend3=models.TextField(blank=True)
    pend4=models.TextField(blank=True)
    exem1=models.TextField(blank=True)
    exem2=models.TextField(blank=True)
    exem3=models.TextField(blank=True)
    comp=models.TextField(blank=True)
    avmark=models.TextField(blank=True)
    spec=models.TextField(blank=True)
    avgrad = models.TextField(blank=True)
    



    def __str__(self):
        return self.user.username


#################     DAYSTAR ##########################
class dStudenthome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    username = models.TextField(blank=True)
    email = models.TextField(blank=True)
    dob = models.TextField(blank=True)
    mno = models.IntegerField(blank=True)
    pschool = models.TextField(blank=True)
    religion = models.TextField(blank=True)
    def __str__(self):
        return self.user.username

class dAprogrammes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    programmme = models.TextField(blank=True)
    syllabus= models.TextField(blank=True)
    status= models.TextField(blank=True)
    intake = models.TextField(blank=True)
    def __str__(self):
        return self.user.username


class dMentoring(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    cmentor = models.TextField(blank=True)
    memail= models.TextField(blank=True)
    dls= models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class dSandPdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    idno = models.IntegerField(blank=True)
    paddress= models.TextField(blank=True)
    town= models.TextField(blank=True)
    hcountry = models.TextField(blank=True)
    residence= models.TextField(blank=True)
    religion= models.TextField(blank=True)
    pcode = models.TextField(blank=True)
    mstatus= models.TextField(blank=True)
    mno= models.TextField(blank=True)
    pemail = models.TextField(blank=True)
    faname= models.TextField(blank=True)
    fmno= models.TextField(blank=True)
    femail = models.TextField(blank=True)
    foccup= models.TextField(blank=True)
    mname= models.TextField(blank=True)
    memail = models.TextField(blank=True)
    mmno= models.TextField(blank=True)
    moccup= models.TextField(blank=True)
    gname = models.TextField(blank=True)
    gmno= models.TextField(blank=True)
    gemail = models.TextField(blank=True)
    goccup = models.TextField(blank=True)


    def __str__(self):
        return self.user.username

class dAttendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    unit1 = models.TextField(blank=True)
    unit2= models.TextField(blank=True)
    unit3= models.TextField(blank=True)
    unit4 = models.TextField(blank=True)
    unit5= models.TextField(blank=True)
    unit6= models.TextField(blank=True)
    unit7 = models.TextField(blank=True)
    att1= models.TextField(blank=True)
    att2= models.TextField(blank=True)
    att3 = models.TextField(blank=True)
    att4= models.TextField(blank=True)
    att5= models.TextField(blank=True)
    att6 = models.TextField(blank=True)
    att7= models.TextField(blank=True)


    def __str__(self):
        return self.user.username

class dFstatement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    date1 =  models.IntegerField(blank=True, null=True)
    date2 =  models.IntegerField(blank=True, null=True)
    date3 =  models.IntegerField(blank=True,null=True)
    date4 =  models.IntegerField(blank=True,null=True)
    date5 =  models.IntegerField(blank=True,null=True)
    date6 =  models.IntegerField(blank=True,null=True)
    date7 =  models.IntegerField(blank=True,null=True)
    date8 =  models.IntegerField(blank=True,null=True)
    date9 =  models.IntegerField(blank=True,null=True)
    date10 =  models.IntegerField(blank=True,null=True)
    date11 =  models.IntegerField(blank=True,null=True)
    dno1 =  models.IntegerField(blank=True,null=True)
    dno2 =  models.IntegerField(blank=True,null=True)
    dno3 =  models.IntegerField(blank=True,null=True)
    dno4 =  models.IntegerField(blank=True,null=True)
    dno5 =  models.IntegerField(blank=True,null=True)
    dno6 =  models.IntegerField(blank=True,null=True)
    dno7 =  models.IntegerField(blank=True,null=True)
    dno8 =  models.IntegerField(blank=True,null=True)
    dno9 =  models.IntegerField(blank=True,null=True)
    dno10 =  models.IntegerField(blank=True,null=True)
    dno11 =  models.IntegerField(blank=True,null=True)
    dtype1 = models.TextField(blank=True)
    dtype2= models.TextField(blank=True)
    dtype3= models.TextField(blank=True)
    dtype4= models.TextField(blank=True)
    dtype5= models.TextField(blank=True)
    dtype6= models.TextField(blank=True)
    dtype7 = models.TextField(blank=True)
    dtype8= models.TextField(blank=True)
    dtype9= models.TextField(blank=True)
    dtype10 = models.TextField(blank=True)
    dtype11= models.TextField(blank=True)
    debit1 =  models.IntegerField(blank=True,null=True)
    debit2 =  models.IntegerField(blank=True,null=True)
    debit3 =  models.IntegerField(blank=True,null=True)
    debit4 =  models.IntegerField(blank=True,null=True)
    debit5 =  models.IntegerField(blank=True,null=True)
    debit6 =  models.IntegerField(blank=True,null=True)
    debit7 =  models.IntegerField(blank=True,null=True)
    debit8 =  models.IntegerField(blank=True,null=True)
    debit9 =  models.IntegerField(blank=True,null=True)
    debit10 =  models.IntegerField(blank=True,null=True)
    debit11 =  models.IntegerField(blank=True,null=True)
    credit1 =  models.IntegerField(blank=True,null=True)
    credit2 =  models.IntegerField(blank=True,null=True)
    credit3 =  models.IntegerField(blank=True,null=True)
    credit4 =  models.IntegerField(blank=True,null=True)
    credit5 =  models.IntegerField(blank=True,null=True)
    credit6 =  models.IntegerField(blank=True,null=True)
    credit7 =  models.IntegerField(blank=True,null=True)
    credit8 =  models.IntegerField(blank=True,null=True)
    credit9 =  models.IntegerField(blank=True,null=True)
    credit10 =  models.IntegerField(blank=True,null=True)
    credit11 =  models.IntegerField(blank=True,null=True)
    totdeb =  models.IntegerField(blank=True,null=True)
    totcred =  models.IntegerField(blank=True,null=True)
  


    def __str__(self):
        return self.user.username

class dPReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField(null=True)
    unit1 = models.TextField(blank=True)
    unit2= models.TextField(blank=True)
    unit3= models.TextField(blank=True)
    unit4 = models.TextField(blank=True)
    unit5= models.TextField(blank=True)
    unit6= models.TextField(blank=True)
    unit7 = models.TextField(blank=True)
    unit8 = models.TextField(blank=True)
    unit9= models.TextField(blank=True)
    unit10= models.TextField(blank=True)
    unit11 = models.TextField(blank=True)
    unit12= models.TextField(blank=True)
    unit13= models.TextField(blank=True)
    unit14= models.TextField(blank=True)
    unit15= models.TextField(blank=True)
    unit16= models.TextField(blank=True)
    unit17= models.TextField(blank=True)
    unit18 = models.TextField(blank=True)
    unit19= models.TextField(blank=True)
    unit20= models.TextField(blank=True)
    unit21 = models.TextField(blank=True)
    att1= models.TextField(blank=True)
    att2= models.TextField(blank=True)
    att3 = models.TextField(blank=True)
    att4= models.TextField(blank=True)
    att5= models.TextField(blank=True)
    att6 = models.TextField(blank=True)
    att7= models.TextField(blank=True)
    att8= models.TextField(blank=True)
    att9= models.TextField(blank=True)
    att10 = models.TextField(blank=True)
    att11= models.TextField(blank=True)
    att12= models.TextField(blank=True)
    att13= models.TextField(blank=True)
    att14 = models.TextField(blank=True)
    att15= models.TextField(blank=True)
    att16= models.TextField(blank=True)
    att17 = models.TextField(blank=True)
    att18= models.TextField(blank=True)
    att19= models.TextField(blank=True)
    att20= models.TextField(blank=True)
    att21= models.TextField(blank=True)
    pend1=models.TextField(blank=True)
    pend2=models.TextField(blank=True)
    pend3=models.TextField(blank=True)
    pend4=models.TextField(blank=True)
    exem1=models.TextField(blank=True)
    exem2=models.TextField(blank=True)
    exem3=models.TextField(blank=True)
    comp=models.TextField(blank=True)
    avmark=models.TextField(blank=True)
    spec=models.TextField(blank=True)
    avgrad = models.TextField(blank=True)
    



    def __str__(self):
        return self.user.username




