from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=30)
    memory = models.IntegerField()
    color = models.CharField(max_length=15)
    quantity = models.IntegerField(default=0)
    img = models.CharField(max_length=500)


class Orders(models.Model):
    phones = models.ForeignKey(Phone, on_delete=models.PROTECT)
    date = models.DateField()


class MyUser(models.Model):
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)


class PhoneCart(models.Model):
    name = models.CharField(max_length=30)
    memory = models.IntegerField()
    color = models.CharField(max_length=15)
    quantity = models.IntegerField(default=0)
    img = models.CharField(max_length=500)
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, default=None, null=True, blank=True)


class PhoneOrder(models.Model):
    name = models.CharField(max_length=30)
    memory = models.IntegerField()
    color = models.CharField(max_length=15)
    quantity = models.IntegerField(default=0)
    img = models.CharField(max_length=500)
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, default=None, null=True, blank=True)
