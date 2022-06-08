import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
# from .forms import FormContactForm
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,'index.html')


def signup(request):
        if request.method == 'POST':
            if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('sid') and request.POST.get('password'):
                post=dbstudent()
                post.fname= request.POST.get('fname')
                post.lname= request.POST.get('lname')
                post.sid= request.POST.get('sid')
                post.password= request.POST.get('password')
                post.save()                
                return render(request, 'login.html')  
        else:
                return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        password = request.POST.get('password')

        try:
            user = dbstudent.empAuth_objects.get(sid=sid,password=password)
            if user is not None:
                return render(request,'index.html',{})
            else:
                print("failed")
                print("They used username:{} and password: {}".format(sid,password))

                return redirect('/')
        except Exception as identifier:
            return redirect('/')
    else:
        return render(request, 'login.html')
        
