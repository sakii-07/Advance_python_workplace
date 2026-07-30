from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = "student_info"


class UserInfo(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    mobile = models.BigIntegerField()

    class Meta:
        db_table = 'user_info'