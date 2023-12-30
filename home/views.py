from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, "index.html", context)

def shop(request):
    context = {}
    return render(request, "shop.html", context)

def loginRegister(request):
    context = {}
    return render(request, "login-resister.html", context)

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