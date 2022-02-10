from pyexpat import model
from django.db import models

# Create your models here.
class Customer(models.Model):
     id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length=100)
     email = models.EmailField(unique=True)