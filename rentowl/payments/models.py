from django.db import models
from orders.models import Order
# Create your models here.
class Payments(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.id