from django.shortcuts import render
from .form import CustomerForm
from .form import LoginForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='home')

def home(request):
    context = {}
    return render(request, "index.html", context)

def shop(request):
    context = {}
    return render(request, "shop.html", context)

def loginRegister(request):
    if request.method == 'POST':
        logset = LoginForm(request.POST)
        uname = request.POST.get('username')
        # mail = request.POST.get('email')
        # phone = request.POST.get('mobile')
        ps = request.POST.get('password')
        # ps1 = request.POST.get('password1')
        userA = authenticate(request, username = uname, password = ps)
        if userA is not None:
            login(request, userA)
            return HttpResponseRedirect('home')
            
    else:
        logset = LoginForm()
    return render(request, "login-resister.html", {'logset':logset})

def Logout(request):
    logout(request)
    return HttpResponse('loginRegister')



def register(request):
    if request.method == 'POST':
        formset = CustomerForm(request.POST)
        uname = request.POST.get('name')
        # mail = request.POST.get('email')
        phone = request.POST.get('mobile')
        ps = request.POST.get('password')
        ps1 = request.POST.get('password1')

        # if formset.is_valid(): 
        #     formset.save()
        #     return HttpResponseRedirect("/loginRegister")
        if ps!=ps1:
            # messages.error(request,'Password and Confirm Password does not match')
            HttpResponse("Your password is not same")
        else:
            new_user = User.objects.create_user(uname, phone, ps)
            new_user.save()
            return HttpResponseRedirect("/loginRegister")
    else:
        formset=CustomerForm()
        return render(request, "register.html", {'formset':formset})

def account(request):
    context = {}
    return render(request, "account.html", context)

def compare(request):
    context = {}
    return render(request, "compare.html", context)

def favourite(request):
    context = {}
    return render(request, "whshlist.html", context)

def cart(request):
    context = {}
    return render(request, "cart.html", context)