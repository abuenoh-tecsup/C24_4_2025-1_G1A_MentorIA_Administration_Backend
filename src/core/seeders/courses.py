from datetime import datetime
from courses.models import Course, Module, Enrollment
from academic.models import Subject, AcademicPeriod
from authentication.models import Professor, Student

def seed_courses():
    print("Creando cursos y módulos...")

    # Obtener datos existentes
    subject = Subject.objects.get(name='Construcción y Pruebas de Software')
    professor_profile = Professor.objects.first()
    student_profile = Student.objects.first()
    academic_period = AcademicPeriod.objects.get(name='2025-I')

    # Crear curso
    course = Course.objects.create(
        subject=subject,
        professor=professor_profile.user
    )

    # Crear módulos
    modules_data = [
        {"title": "Introducción al curso", "description": "Presentación del temario y objetivos", "module_order": 1},
        {"title": "Metodologías de desarrollo", "description": "Estudio de metodologías ágiles y tradicionales", "module_order": 2},
        {"title": "Pruebas de software", "description": "Tipos de pruebas y herramientas", "module_order": 3},
    ]

    for mod in modules_data:
        Module.objects.create(course=course, **mod)

    # Inscribir estudiante
    Enrollment.objects.create(
        student=student_profile,
        course=course,
        period=academic_period,
        status='active',
    )

    print("Cursos, módulos e inscripciones creados correctamente.")
