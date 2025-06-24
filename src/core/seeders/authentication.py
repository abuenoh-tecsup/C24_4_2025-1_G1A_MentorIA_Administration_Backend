from datetime import date
from authentication.models import User, Professor, Student
from academic.models import Career

def seed_authentication():

    print("Creando usuarios, profesores y estudiantes...")

    # Admin user
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123',
        first_name='Admin',
        last_name='User',
        role='admin'
    )

    # Profesor user
    prof_user = User.objects.create_user(
        username='profesor1',
        email='profesor1@example.com',
        password='profpass123',
        first_name='Juan',
        last_name='Perez',
        role='professor'
    )
    prof_profile = Professor.objects.create(
        user=prof_user,
        employee_code='EMP001',
        hire_date=date(2020, 3, 1),
        department='Software Engineering',
        academic_title='PhD in Computer Science',
        office_location='Building A, Room 101',
        status='active'
    )

    # Estudiante user
    student_user = User.objects.create_user(
        username='estudiante1',
        email='estudiante1@example.com',
        password='studpass123',
        first_name='Maria',
        last_name='Gonzalez',
        role='student'
    )
    career = Career.objects.get(code='C24')
    student_profile = Student.objects.create(
        user=student_user,
        career=career,
        student_code='STU001',
        enrollment_date=date(2023, 3, 1),
        current_semester=3,
        average_grade=15.5,
        status='active'
    )

    print("Usuarios creados correctamente.")
