from django.db import models
from django.conf import settings

class Task(models.Model):
    module = models.ForeignKey('courses.Module', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    
    class Meta:
        db_table = 'task'
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['due_date']
    
    def __str__(self):
        return f"{self.title} - {self.module}"

class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('submitted', 'Submitted'),
        ('graded', 'Graded'),
    ]
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    grade = models.FloatField(null=True, blank=True)
    comments = models.TextField(blank=True, null=True)
    file_url = models.URLField(blank=True, null=True)
    
    class Meta:
        db_table = 'submission'
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'
        unique_together = ['task', 'user']
    
    def __str__(self):
        return f"{self.user.username} - {self.task.title}"