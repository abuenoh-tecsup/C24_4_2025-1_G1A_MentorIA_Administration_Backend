from django.db import models
from django.conf import settings

class Material(models.Model):
    TYPE_CHOICES = [
        ('video', 'Video'),
        ('document', 'Document'),
        ('link', 'Link'),
        ('other', 'Other'),
    ]
    
    module = models.ForeignKey('courses.Module', on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='document')
    resource_url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'material'
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
        ordering = ['creation_date']
    
    def __str__(self):
        return f"{self.title} - {self.module}"

class FavoriteMaterial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='favorited_by')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'favorite_material'
        verbose_name = 'Material Favorito'
        verbose_name_plural = 'Materiales Favoritos'
        unique_together = ['user', 'material']
    
    def __str__(self):
        return f"{self.user.username} - {self.material.title}"