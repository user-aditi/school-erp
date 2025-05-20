from django.shortcuts import render
from .models import Student, Attendance

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'students/attendance_list.html', {'attendances': attendances})