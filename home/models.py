from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 30)
    # email = models.EmailField()
    mobile = models.IntegerField()
    password = models.CharField(max_length = 10)
    password1 = models.CharField(max_length = 10)


class Login(models.Model):
    username = models.CharField(max_length = 30, unique = True)
    # email = models.EmailField()
    # mobile = models.IntegerField()
    password = models.CharField(max_length = 10, unique = True)
    password1 = models.CharField(max_length = 10, unique = True)

    def __str__(self):
        return self.name
    

