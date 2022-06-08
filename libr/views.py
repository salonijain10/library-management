import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import BookForm
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth



# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_signup(request):
        if request.method == 'POST':
            if request.POST.get('email') and request.POST.get('password'):
                post=dbadmin()
                post.email= request.POST.get('email')
                post.password= request.POST.get('password')
                post.save()                
                return render(request, 'login_admin.html')  
        else:
                return render(request,'admin_signup.html')

def login_admin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = dbadmin.empAuth_objects.get(email=email,password=password)
            if user is not None:
                return render(request,'adminhome.html',{})
            else:
                print("failed")
                print("They used username:{} and password: {}".format(email,password))

                return redirect('/')
        except Exception as identifier:
            return redirect('/')
    else:
        return render(request, 'login_admin.html')

def addbook(request):
    if request.method == 'POST':
        if request.POST.get('bname') and request.POST.get('author') and request.POST.get('isbn') and request.POST.get('category'):
            post=bookdb()
            post.bname= request.POST.get('bname')
            post.author= request.POST.get('author')
            post.isbn= request.POST.get('isbn')
            post.category= request.POST.get('category')
            post.save()                
            return render(request, 'viewbook.html')  
    else:
            return render(request,'addbook.html')

def adminhome(request):
    return render(request,'adminhome.html')

def viewbook(request): 
    books = bookdb.empBook_objects.all()
    return render(request,"viewbook.html",{'books':books})

def edit(request, id):  
    books = bookdb.empBook_objects.get(id=id)  
    return render(request,'edit.html', {'books':books})  

def update(request, id):  
    books = bookdb.empBook_objects.get(id=id)  
    form = BookForm(request.POST, instance = books)  
    if form.is_valid():  
        form.save()  
        return redirect("/viewbook")  
    return render(request, 'edit.html', {'books':books})

def delete(request, id):  
    books = bookdb.empBook_objects.get(id=id)  
    books.delete()  
    return redirect("/viewbook")    


        
