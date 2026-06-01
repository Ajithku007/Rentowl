from django.db import models
from listings.models import Products
from accounts.models import User
# Create your models here.

class Order(models.Model):
    Status_choices=(('requested','Requested'),('accepted','Accepted'),('active','Active'),('rejected','Rejected'),('pending','Pending'),('canceled','Canceled'))
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    borrower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrowed_orders')
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=30,choices=Status_choices,default='requested')
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"order {self.id} - { self.product.title }"

    def rental_days(self):
        return (self.end_date - self.start_date)+1
