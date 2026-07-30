from rest_framework import serializers
from .models import StudentInfo

class StudentInfoSeri(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'