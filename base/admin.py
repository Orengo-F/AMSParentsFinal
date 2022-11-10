from django.contrib import admin
from .models import Studenthome,Aprogrammes,Mentoring, SandPdetails, Attendance, Fstatement,PReport

# Register your models here.
admin.site.register(Studenthome)
admin.site.register(Aprogrammes)
admin.site.register(Mentoring)
admin.site.register(SandPdetails)
admin.site.register(Attendance)
admin.site.register(Fstatement)
admin.site.register(PReport)