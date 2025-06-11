from django.db import models
from django.conf import settings

class Evaluation(models.Model):
    module = models.ForeignKey('courses.Module', on_delete=models.CASCADE, related_name='evaluations')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    time_limit = models.IntegerField(help_text="Tiempo límite en minutos")
    
    class Meta:
        db_table = 'evaluation'
        verbose_name = 'Evaluación'
        verbose_name_plural = 'Evaluaciones'
    
    def __str__(self):
        return f"{self.title} - {self.module}"

class Question(models.Model):
    TYPE_CHOICES = [
        ('multiple_choice', 'Multiple Choice'),
        ('open', 'Open'),
    ]
    
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='questions')
    statement = models.TextField()
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='multiple_choice')
    options = models.JSONField(blank=True, null=True)
    correct_answer = models.TextField()
    
    class Meta:
        db_table = 'question'
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
    
    def __str__(self):
        return f"Q: {self.statement[:50]}..."

class EvaluationAttempt(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='attempts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='evaluation_attempts')
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='in_progress')
    score = models.FloatField(null=True, blank=True)
    comments = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'evaluation_attempt'
        verbose_name = 'Intento de Evaluación'
        verbose_name_plural = 'Intentos de Evaluación'
    
    def __str__(self):
        return f"{self.user.username} - {self.evaluation.title}"

class QuestionAnswer(models.Model):
    attempt = models.ForeignKey(EvaluationAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'question_answer'
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        unique_together = ['attempt', 'question']
    
    def __str__(self):
        return f"{self.attempt.user.username} - Q{self.question.id}"