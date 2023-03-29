from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.forms import CharField


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=250)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)



class register(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=300)
