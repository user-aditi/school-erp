from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from .models import Student, Attendance

# Unregister default User admin if already registered
admin.site.unregister(User)

# Custom User Admin (optional)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Attendance)


