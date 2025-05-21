from django.shortcuts import render
from .models import Student, Attendance
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .serializers import AttendanceSerializer

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
    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)