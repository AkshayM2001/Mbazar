from django.shortcuts import render
from .form import CustomerForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    context = {}
    return render(request, "index.html", context)

def shop(request):
    context = {}
    return render(request, "shop.html", context)

def loginRegister(request):
    return render(request, "register.html")

def register(request):
    if request.method == 'POST':
        formset = CustomerForm(request.POST)
        uname = request.POST.get('name')
        mail = request.POST.get('email')
        phone = request.POST.get('mobile')
        ps = request.POST.get('password')
        ps1 = request.POST.get('password1')

        new_user = User.objects.create_user(uname, mail, phone, ps)
        new_user.save()


        if formset.is_valid():
            
            formset.save()
            return HttpResponseRedirect("/home")

    else:
        formset = CustomerForm()
        return render(request, "login-resister.html", {'formset':formset})

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