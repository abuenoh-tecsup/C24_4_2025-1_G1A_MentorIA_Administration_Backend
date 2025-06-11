from django.db import models
from django.conf import settings

class Course(models.Model):
    subject = models.ForeignKey('academic.Subject', on_delete=models.CASCADE, related_name='courses')
    professor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='taught_courses')
    
    class Meta:
        db_table = 'course'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    def __str__(self):
        return f"{self.subject.name} - {self.professor.get_full_name()}"

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'module'
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.course} - {self.title}"

class Enrollment(models.Model):
    student = models.ForeignKey('authentication.Student', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    period = models.ForeignKey('academic.AcademicPeriod', on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=20, default='active')
    enrollment_date = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'enrollment'
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'
        unique_together = ['student', 'course', 'period']
    
    def __str__(self):
        return f"{self.student} - {self.course}"

class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='announcements')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateTimeField()
    
    class Meta:
        db_table = 'announcement'
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'
        ordering = ['-publication_date']
    
    def __str__(self):
        return f"{self.title} - {self.course}"