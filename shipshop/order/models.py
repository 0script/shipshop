from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

from product.models import Product

# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(User,related_name='orders', on_delete=models.CASCADE)
    first_name=models.CharField( max_length=100)
    last_name=models.CharField( max_length=100)
    phone=models.CharField( max_length=100)
    email=models.CharField( max_length=100)
    address=models.CharField( max_length=255)
    place=models.CharField( max_length=100)
    ordered_date=models.DateTimeField(auto_now_add=True)
    # is_delivered=models.BooleanField(default=False)
    # is_paid=models.BooleanField(default=False)
    # e-pay
    paid_ammount=models.DecimalField( max_digits=10, decimal_places=2,blank=True,null=True)
    # api_token=............................................

    class Meta:
        ordering=('-ordered_date',)
    
    def __str__(self):
        return self.first_name
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
    