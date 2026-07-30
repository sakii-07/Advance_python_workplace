from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=32,primary_key=True)
    mobile=models.BigIntegerField(unique=True)
    password=models.CharField(max_length=32)
    created_at=models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'userinfo'

class Medicine(models.Model):
    medicine_name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    price=models.BigIntegerField()
    quantity=models.IntegerField()
    mfg_date=models.DateField()
    exp_date=models.DateField()
    description = models.TextField()

    class Meta:
        db_table='medicine'

    def __str__(self):
        return self.medicine_name
    