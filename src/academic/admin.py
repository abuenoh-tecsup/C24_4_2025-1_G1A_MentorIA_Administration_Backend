from django.contrib import admin
from .models import Career

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    search_fields = ['name']  # ajusta según el campo que uses para nombre
    list_display = ['id', 'name']  # opcional, para mostrar en la tabla
