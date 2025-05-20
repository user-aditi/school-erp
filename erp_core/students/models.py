from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return self.name