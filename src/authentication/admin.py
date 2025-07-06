# authentication/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Professor, Student

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Añadimos 'google_id' a los fieldsets para que sea visible y editable
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('phone', 'profile_picture_url', 'role', 'google_id') # <-- ¡AQUÍ ESTÁ EL CAMBIO!
        }),
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'google_id') # <-- Opcional: para verlo en la lista
    list_filter = ('role',)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'google_id') # <-- Opcional: para buscar por google_id
    ordering = ('username',)

# Admin para el modelo Professor
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_code', 'department', 'academic_title', 'status')
    list_filter = ('status', 'department')
    search_fields = ('user__first_name', 'user__last_name', 'employee_code')
    autocomplete_fields = ['user']

# Admin para el modelo Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_code', 'career', 'current_semester', 'average_grade', 'status')
    list_filter = ('status', 'career')
    search_fields = ('user__first_name', 'user__last_name', 'student_code')
    autocomplete_fields = ['user', 'career']