from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("homepage",views.homepage,name="homepage"),
    path("strathmorelogin",views.strathmorelogin,name="strathmorelogin"),
    path('studentreg',views.studentreg,name='studentreg'),
    path('strathmore',views.strathmore,name='strathmore'),
    path('daystar',views.daystar,name='daystar'),
    path('shome',views.shome,name='shome'),
    path('sstudentdetails',views.sstudentdetails,name='sstudentdetails'),
    path('sattendance',views.sattendance,name='sattendance'),
    path('spreport',views.spreport,name='spreport'),
    path('sfeestructure',views.sfeestructure,name='sfeestructure'),
    path('sfeestatement',views.sfeestatement,name='sfeestatement'),
    path('spayfee',views.spayfee,name='spayfee'),
    path('dsstudenthome',views.dsstudenthome,name='dsstudenthome'),

    
]
