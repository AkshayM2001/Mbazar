from django.conf import UserSettingsHolder
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from home import form

# Create your views here.

def home(request):
    return render(request, "index.html")

def shop(request):
    context = {}
    return render(request, "shop.html", context)

def register(request):
    if request.method == 'POST':
        # formset = SignUpfm(request.POST)
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if len(fname) > 3 and len(lname)>3:
            user = UserSettingsHolder.objects.create_user(username=username, first_name=fname, last_name=lname, email=email)
            user = authenticate(username=username, password=password1, password2 = password2)
            if user is not None:
                login(request,user)
                messages.info(request,"Username already exists.")
                return redirect('/home')
            else:
                return render(request,'accounts/signup.html', {'form' : form})

        # if formset.is_valid(): 
        #     formset.save()
        #     messages.success(request, "Your Account has been successfully created!!!")
        #     return redirect("/loginRegister")
        

    # else:
    #     formset = SignUpfm()

    # return render(request, "register.html", {'formset': formset})

def loginRegister(request):
    # if request.method == 'POST':
    #     username = request.POST['username1']
    #     password1 = request.POST['password11']

    #     user = authenticate(username = username, password1 = password1)

    #     if user is not None:
    #         login(request, user)
    #         fname = user.first_name
    #         return render(request, "/home", {'fname': fname})
        
    #     else:
    #         messages.error(request, "Bad Credentials")
    #         return redirect("/loginRegister", {'first_name': fname})
    return render(request, "login-resister.html")


def signout(request):
    pass