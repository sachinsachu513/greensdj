from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def greetings(request):
    # msg='''<h1> greetings! welcome sachin <h1> <body text ='brown' bgcolor='white'>
    # <h1> for new registration <a href="/reg">click here </a> </h1><br>
    # <h2> for login<a href='/home'>click here </a><br>
    # <h3>ipl points table <a href='/second/ipltable'>click here </a><br>
    # <h3>product purchase <a href='/second/getprice'>click here </a><br>
    # <h3>to database <a href='/admin/'>click here</a><br>
    # <h3> registered  student <a href='/model/database'> click here </a>
    # <h3> simple form without html <a href='/model/register'> click here</a>
    # <h3> simple form without html2 <a href='/model/simple'> click here</a>
    #
    #
    #
    # '''
    # return HttpResponse(msg)
    return render(request,"home\greetings.html")
def homepage(request):
   return render(request,"first\SMPL.html")
def loginpage(request):
  return render(request,"first\SMPL.html")
def registerpage(request):
  return render(request,"first\sample.html")