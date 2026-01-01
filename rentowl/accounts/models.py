from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone=models.IntegerField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    profile_image=models.ImageField(upload_to='profile_images',blank=True,null=True)

    def __str__(self):
        return self.username