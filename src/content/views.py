from rest_framework import viewsets
from .models import Material, FavoriteMaterial, GeneratedContent
from .serializers import MaterialSerializer, FavoriteMaterialSerializer, GeneratedContentSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class FavoriteMaterialViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMaterial.objects.all()
    serializer_class = FavoriteMaterialSerializer

class GeneratedContentViewSet(viewsets.ModelViewSet):
    queryset = GeneratedContent.objects.all()
    serializer_class = GeneratedContentSerializer
