from django.http import HttpResponse
from django.shortcuts import render
from pyqrcode import QRCode

from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status
from myapp.serializers import UserInfoSerializer
from fastapi import FastAPI

app=FastAPI()

# # Create your views here.
# @api_view(['GET','POST'])
# def Register(request):
#     if request.method=='POST':
#         Username=request.POST['Username']
#         Email=request.POST['email']
#         Password=request.POST['password']
#         print('username is {} and email is {} and password is {}'.format(Username,Email,Password))
#         serializer=UserInfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#     else:
#         # return HttpResponse('User register successfully')
#         return render(request,'myapp/signup.html')

@app.get('/')
def Login(request):
    return 'FastAPI'
