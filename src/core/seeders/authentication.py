from datetime import date
from authentication.models import User, Professor, Student
from academic.models import Career

def seed_authentication():

    print("Creando usuarios, profesores y estudiantes...")

    # Admin user 1
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123',
        first_name='Admin',
        last_name='User',
        role='admin',
        google_id=None
    )

    # Nuevo admin user (Sonaly Vania)
    sonaly_admin = User.objects.create_superuser(
        username='sonaly',
        email='sonaly.sifuentes@tecsup.edu.pe',
        password='adminpass123',
        first_name='Sonaly',
        last_name='Vania',
        role='admin',
        google_id=None
    )

    # Profesor user (Álvaro Bueno)
    prof_user = User.objects.create_user(
        username='alvaro.bueno',
        email='alvaro.bueno@tecsup.edu.pe',
        password='profpass123',
        first_name='Alvaro',
        last_name='Bueno',
        role='professor',
        google_id=None
    )
    prof_profile = Professor.objects.create(
        user=prof_user,
        employee_code='EMP002',
        hire_date=date(2021, 2, 15),
        department='Sistemas',
        academic_title='Ingeniero de Sistemas',
        office_location='Edificio B, Oficina 202',
        status='active'
    )

    # Estudiante user (Eduardo Bullón)
    student_user = User.objects.create_user(
        username='eduardo.bullon',
        email='eduardo.bullon@tecsup.edu.pe',
        password='studpass123',
        first_name='Eduardo',
        last_name='Bullón',
        role='student',
        google_id=None
    )
    career = Career.objects.get(code='C24')
    student_profile = Student.objects.create(
        user=student_user,
        career=career,
        student_code='STU002',
        enrollment_date=date(2023, 3, 1),
        current_semester=3,
        average_grade=15.5,
        status='active'
    )

    print("Usuarios creados correctamente.")
