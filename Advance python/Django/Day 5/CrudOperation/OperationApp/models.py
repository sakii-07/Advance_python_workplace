from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32, unique=True)
    mobile = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'userinfo'
