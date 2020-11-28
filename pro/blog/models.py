from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email =models.CharField(max_length=50)
class posts(models.Model):
    name= models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    decription = models.CharField(max_length=100)