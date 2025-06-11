from django.db import models
from django.conf import settings

class Forum(models.Model):
    module = models.ForeignKey('courses.Module', on_delete=models.CASCADE, related_name='forums')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_forums')
    title = models.CharField(max_length=200)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'forum'
        verbose_name = 'Foro'
        verbose_name_plural = 'Foros'
        ordering = ['-creation_date']
    
    def __str__(self):
        return f"{self.title} - {self.module}"

class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'comment'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['creation_date']
    
    def __str__(self):
        return f"{self.user.username} - {self.forum.title}"