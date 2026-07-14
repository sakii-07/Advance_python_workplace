from django.db import models

# Create your models here.
class StudentIfo(models.Model):
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    email = models.CharField(max_length=32, unique=True)
    mobile = models.BigIntegerField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    course = models.CharField(max_length=12)
    semester = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True, primary_key=True)
    password = models.CharField(max_length=32)
    created_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'studentinfo'
