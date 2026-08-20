from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=50)
    seller_name = models.CharField(max_length=50)
    discount_percent = models.FloatField()
    rating = models.FloatField()
    status = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "product"