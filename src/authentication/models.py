from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('professor', 'Professor'),
        ('admin', 'Admin'),
    ]
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture_url = models.URLField(blank=True, null=True)
    # google_id se mantiene, es opcional para la creación
    google_id = models.CharField(max_length=255, unique=True, blank=True, null=True) 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Professor(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('retired', 'Retired'),
        ('on_leave', 'On Leave'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor_profile')
    employee_code = models.CharField(max_length=20, unique=True)
    hire_date = models.DateField()
    department = models.CharField(max_length=100)
    academic_title = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
    class Meta:
        db_table = 'professor'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
    
    def __str__(self):
        return f"Prof. {self.user.get_full_name()} - {self.employee_code}"

class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('graduated', 'Graduated'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    career = models.ForeignKey('academic.Career', on_delete=models.CASCADE, related_name='students')
    student_code = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateField()
    current_semester = models.IntegerField(default=1)
    average_grade = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
    class Meta:
        db_table = 'student'
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.student_code}"