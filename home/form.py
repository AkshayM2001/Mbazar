from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'mobile', 'password', 'password1']
        

