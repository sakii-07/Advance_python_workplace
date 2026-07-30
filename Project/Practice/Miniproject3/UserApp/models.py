from django.db import models

# Create your models here.

class UserInformation(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50,unique=True)
    salary = models.FloatField()

    class Meta:
        db_table = 'customer_info'
