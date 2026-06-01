from django.db import models
from accounts.models import User
# Create your models here.
class Dashboard(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    rent=models.DecimalField(max_digits=10,default=0,decimal_places=2)
    spent=models.DecimalField(max_digits=10,default=0,decimal_places=2)

    def __str__(self):
        return self.user.username
