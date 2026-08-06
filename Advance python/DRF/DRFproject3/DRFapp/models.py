from django.db import models

# Create your models here.
class LaptopInfo(models.Model):
    laptop_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'laptop_info'