from django.shortcuts import render
from django.http import HttpResponse
def login(request,username):
    return render(request,'login/login.html',context={"name":username, "age":8})
# Create your views here.
