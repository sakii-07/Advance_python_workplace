from django.db import models

# Create your models here.

class Question(models.Model):
    qno = models.AutoField(primary_key=True)
    qtext = models.CharField(max_length=100)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)
    corr_answer = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'question'

class UserInfo(models.Model):
    username =  models.CharField(max_length=100, primary_key=True)
    password =  models.CharField(max_length=100)
    mobile =  models.BigIntegerField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user_info'