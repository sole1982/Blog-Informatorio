from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario', default='.static/img/usu_default_navidad.jpg')
    
    def get_absolute_url(self):
        return reverse('index')
    