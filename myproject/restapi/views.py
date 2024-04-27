from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import userregisterserializer
from rest_framework import status

from .models import userregister

@api_view(["GET"])
def getuser(request):
    user=userregister.objects.all()
    serializer=userregisterserializer(user,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def createuser(request):
    newuser=userregisterserializer(data=request.data)
    if newuser.is_valid():
        newuser.save()
    return Response(newuser.error_messages,status=status.HTTP_200_OK)


@api_view(["DELETE"])
def deleteuser(request,id):
    user=userregister.objects.get(id=id)
    newuser=userregisterserializer(data=request.data)
    user.delete()
    return Response(newuser.error_messages,status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def updateuser(request,id):
    user=userregister.objects.get(id=id)
    newuser=userregisterserializer(user,data=request.data)
    if newuser.is_valid():
        newuser.save()
        return Response(newuser.data,status=status.HTTP_200_OK)

