from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username =  models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=50, unique=True)
    password =  models.CharField(max_length=100)
    mobile =  models.BigIntegerField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user_info'

    def __str__(self):
        return self.username

class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Trainer"

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    purchase_date = models.DateField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "Equipment"

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "Attendance"

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_mode = models.CharField(max_length=30)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=20)

    class Meta:
        db_table = "Payment"
        
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    feedback_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Feedback"
