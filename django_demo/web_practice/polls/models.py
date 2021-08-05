from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

class Info(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    eamil = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
