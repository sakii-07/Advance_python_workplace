from django.db import models

# Create your models here.
class Employee(models.Model):
    empId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField() 
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    salary = models.FloatField()
    joiningDate = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = "Employee_info"