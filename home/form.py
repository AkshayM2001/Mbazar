from django.forms import ModelForm
from .models import Customer
from .models import Login

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'mobile', 'password', 'password1']
        
class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']
        

