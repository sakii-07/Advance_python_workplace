from django.db import models

# Create your models here.
class SigninInfo(models.Model):
    uname = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32, unique=True)
    mobile = models.BigIntegerField(max_length=12)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'signin_info'
