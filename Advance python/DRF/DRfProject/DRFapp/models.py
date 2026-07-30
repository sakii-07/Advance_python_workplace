from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    mobile = models.BigIntegerField()

    class Meta:
        db_table = 'user_info'