from django.db import models

# Create your models here.
#-----------   CATEGORY   ----------
class Category(models.Model):
    category_name=models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


#------   PRODUCTS  --------
from accounts.models import User

class Products(models.Model):
    title=models.CharField(max_length=30)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='products')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    rent_price=models.IntegerField()
    deposit_price = models.IntegerField(default=0)
    location=models.CharField(max_length=300)
    description=models.TextField(blank=True)
    available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title