from django.shortcuts import render
from .models import studenttable,database
from.forms import registerform,myform

from django.http import HttpResponse

def getstudent(request):
    student=studenttable.objects.all()
    return render(request,"modelapp//studentdetails.html",context={"student":student})


def register(request):
    form=registerform()
    return render(request,"modelapp//register.html",context={"form":form})

def simple(request):
 form= myform()
 return render(request,"modelapp//samplem.html",context={"form":form})


def submitform(request):
  if request.method=='POST':
     if (request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('phone_number') and request.POST.get('email_id') and request.POST.get('password') and request.POST.get('confirm_password')):
        reg=database()
        reg.firstname=request.POST.get('firstname')
        reg.lastname=request.POST.get('lastname')
        reg.phone_number=request.POST.get('phone_number')
        reg.email_id=request.POST.get('email_id')
        reg.password=request.POST.get('password')
        reg.confirm_password=request.POST.get('confirm_password')
        reg.save()
     else:
        return HttpResponse('<h1>  fields not founded </h1>')



  form=registerform()
  return render(request,"modelapp//register.html",context={"form":form})


def getting(request):
    details=database.objects.all()
    return render(request,'modelapp/database.html',context={"details":details})