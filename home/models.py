from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.name
    
