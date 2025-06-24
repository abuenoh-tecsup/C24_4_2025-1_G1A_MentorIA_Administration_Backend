from datetime import datetime
from django.utils.timezone import make_aware
from academic.models import Career, Subject, AcademicPeriod

def seed_academic():
    print("Creando carreras, materias y periodo académico...")

    # Crear carrera
    career = Career.objects.create(
        code="C24",
        name="Diseño y Desarrollo de Software"
    )

    # Crear materia
    subject = Subject.objects.create(
        name="Construcción y Pruebas de Software"
    )

    # Fechas del primer semestre 2025
    start_date = make_aware(datetime(2025, 2, 1, 0, 0, 0))  # 1 feb 2025
    end_date = make_aware(datetime(2025, 6, 30, 23, 59, 59))  # 30 jun 2025

    # Crear período académico
    academic_period = AcademicPeriod.objects.create(
        name="2025-I",
        year=2025,
        term=1,
        start_date=start_date,
        end_date=end_date
    )
