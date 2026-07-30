from django.db import models

# Create your models here.

class CustomerInfo(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    salary = models.FloatField()

    class Meta:
        db_table = 'customer_info'