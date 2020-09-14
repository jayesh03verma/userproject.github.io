from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact , Register , Todo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout 
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.utils import timezone



# password for test user is Flair$1010
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        register = Register(name=name, email=email, phone=phone, date = datetime.today())
        register.save()
        messages.success(request, 'Your Registration has done successfully!')
    return render(request, 'register.html')    

def todo(request):
    if request.method == "POST":
     Date = request.POST.get('Date')
     text = request.POST.get('text')    
     todo = Todo(text=text, Date=Date, date = datetime.today())
     todo.save()
     messages.success(request, 'Your items added successfully!')
    return render(request, 'todo.html')


