from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)

    class Meta:
        db_table = 'userinfo'
