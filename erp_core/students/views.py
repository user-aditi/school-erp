from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Student, Attendance
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .serializers import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'students/attendance_list.html', {'attendances': attendances})

class StudentListAPI(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class AttendanceCreateAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Force-set teacher from authenticated user
        data = request.data.copy()
        data['teacher'] = request.user.id
        
        serializer = AttendanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)