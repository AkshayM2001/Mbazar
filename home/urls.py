"""
URL configuration for Bazar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views1

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views1.home),
    path('home', views1.home),
    path('shop', views1.shop),
    path('loginRegister', views1.loginRegister),
    path('logout', views1.Logout),
    path('Register', views1.register),
    path('account', views1.account),
    path('favourite', views1.favourite),
    path('compare', views1.compare),
    path('cart', views1.cart),

]
