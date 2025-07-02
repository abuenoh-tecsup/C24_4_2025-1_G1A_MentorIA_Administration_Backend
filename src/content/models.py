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
    text_plain = models.TextField(blank=True, null=True)
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
    
class GeneratedContent(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('summary', 'Resumen'),
        ('flashcards', 'Flashcards'),
    ]
    
    OUTPUT_FORMAT_CHOICES = [
        ('text', 'Texto'),
        ('json', 'JSON'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='generated_contents')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='generated_contents')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    output_format = models.CharField(max_length=10, choices=OUTPUT_FORMAT_CHOICES)
    content = models.TextField()  # Puedes guardar texto plano o JSON serializado como string
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'generated_content'
        verbose_name = 'Contenido Generado'
        verbose_name_plural = 'Contenidos Generados'
        ordering = ['-creation_date']

    def __str__(self):
        return f"{self.user.username} - {self.material.title} - {self.content_type}"
