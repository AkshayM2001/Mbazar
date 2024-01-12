from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import LoginForm
from .form import SignUpfm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "index.html")

def shop(request):
    context = {}
    return render(request, "shop.html", context)

def register(request):
    if request.method == 'POST':
        formset = SignUpfm(request.POST)

        if formset.is_valid(): 
            formset.save()
            messages.success(request, "Your Account has been successfully created!!!")
            return redirect("/loginRegister")
        

    else:
        formset = SignUpfm()

    return render(request, "register.html", {'formset': formset})

def loginRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username = username, password1 = password1)

        if user is not None:
            login(request, user)
            first_name = user
            return render("/home")
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect("/loginRegister")

    return render(request, "login-resister.html" {'first_name': first_name})

def signout(request):
    pass