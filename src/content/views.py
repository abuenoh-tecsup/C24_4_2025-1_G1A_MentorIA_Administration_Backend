from rest_framework import viewsets
from .models import Material, FavoriteMaterial
from .serializers import MaterialSerializer, FavoriteMaterialSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class FavoriteMaterialViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMaterial.objects.all()
    serializer_class = FavoriteMaterialSerializer