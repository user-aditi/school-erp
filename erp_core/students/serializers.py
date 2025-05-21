from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Attendance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(
        read_only=True,  # Add this to make teacher auto-assigned
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'date', 'status', 'teacher']