from django.db import models

# Create your models here.

class Product_info(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField()
    description=models.CharField(max_length=100)
    seller_name=models.CharField(max_length=100)
    discount_percent=models.IntegerField()
    rating=models.FloatField()
    status=models.CharField(max_length=100)
    created_date=models.DateField(auto_now_add=True)

    class Meta():
        db_table='product1'