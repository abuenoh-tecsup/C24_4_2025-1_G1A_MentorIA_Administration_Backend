from django.db import models

class Career(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'career'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'subject'
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
    
    def __str__(self):
        return self.name

class AcademicPeriod(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    term = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    class Meta:
        db_table = 'academic_period'
        verbose_name = 'Período Académico'
        verbose_name_plural = 'Períodos Académicos'
        unique_together = ['year', 'term']
    
    def __str__(self):
        return f"{self.name} - {self.year}"