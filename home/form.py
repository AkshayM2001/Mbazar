from django.forms import ModelForm
from .models import Customer
from .models import Login
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class CustomerForm(ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['name', 'mobile', 'password', 'password1']
        
#class LoginForm(UserCreationForm):
 #   def __init__(self, *args, **kwargs):
  #     super(LoginForm, self).__init__(*args, **kwargs)
    #    del self.fields['password1']
 #      del self.fields['password2']

 #   class Meta:
#        model = User
#         fields = ['name', 'mobile', 'password', 'password1']
#        fields = ['username', 'password1']
        # labels = {'email': 'Email'}
        # exclude = ['password2']

    # def __init__(self, 'ho.forms.LoginForm') -> None:
    #     super(LoginForm).__init__(*args, **kwargs)
    #     del self.fields['password2']



class SignUpfm(UserCreationForm):
    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput)
    # PASSWORD2 IS Name attribute in html page 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}

