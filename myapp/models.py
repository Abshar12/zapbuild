from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class User(AbstractUser):
    is_client  = models.BooleanField(default=False)
    is_manager  = models.BooleanField(default=False)
    is_employee  = models.BooleanField(default=False)

    def __str__(self):
        return self.username

@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)


class Client(models.Model):
    user = models.OneToOneField(User,related_name='client',on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(User,related_name='manager',on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Employee(models.Model):
    user = models.OneToOneField(User,related_name='employee',on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Status(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title