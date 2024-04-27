import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def ipltable(request):
    date=datetime.datetime.now().date()
    time=datetime.datetime.now().time()
    dict={"org":"jio","oname":"mukesh","date":date,"time":time}
    return render(request,"ipl table\ipl.html",context=dict)
def secondapp(request):
    return HttpResponse("welcome to second app")

def getprice(request):
    return render(request,"product\getprice.html")

def totalprice(request):
  lap=int(request.GET["laptop"])
  mob=int(request.GET["phone"])
  tab=int(request.GET["tablet"])
  mou=int(request.GET["mouse"])
  totalprice=lap+mob+tab+mou
  return render(request,"product/result.html",context={"total":totalprice})


