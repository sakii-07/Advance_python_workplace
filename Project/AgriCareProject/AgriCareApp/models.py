from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=32)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user_info'

class Product(models.Model):
    product_name = models.CharField(max_length=200, primary_key=True)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/')
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'Products'