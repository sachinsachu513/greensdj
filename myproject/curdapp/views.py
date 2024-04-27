from django.shortcuts import render, redirect

# Create your views here.
from.models import employees1
from.forms import employeeform
from django.http import HttpResponse
from django.core import serializers
def getemployeedetails(request):
    emp=employees1.objects.all()
    # data=serializers.serialize("json",emp)
    # return HttpResponse(data,content_type="application/json")
    return render(request,"curd//employdetails.html",context={"emp":emp})
def createemployees(request):
    form=employeeform()
    if request.method=="POST":
        form=employeeform(request.POST)
        if form.is_valid():
          form.save()
          return HttpResponse("""<h1> new employ data sucessfully added </h1>
          
          <h1> <a href="/curd/empdetail"> click here </a>view employ details</h2>
          
          
          
          """

                              )

    return render(request,'curd//addemployees.html',context={'form':form})



def deleteemploy(request,id):
    emp=employees1.objects.get(id=id)
    emp.delete()
    return redirect("/curd/empdetail")

def updateemploy(request,id):
    emp=employees1.objects.get(id=id)
    if request.method=='POST':
        form=employeeform(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponse("""<h1> employ data updated suceesfully </h1>

                     <h1> <a href="/curd/empdetail"> click here </a>view employ details</h2>
                   """)
    return render(request,"curd//update.html",context={"emp":emp})



