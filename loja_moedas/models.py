from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from core import settings

# Create your models here.


class UserProfilePhoto(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Coin(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coins/', null=True, blank=True)
    description = models.TextField(verbose_name='Descrição:')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
