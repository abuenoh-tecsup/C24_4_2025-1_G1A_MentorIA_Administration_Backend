from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaterialViewSet, FavoriteMaterialViewSet, GeneratedContentViewSet

router = DefaultRouter()
router.register(r'materials', MaterialViewSet)
router.register(r'favorites', FavoriteMaterialViewSet)
router.register(r'generated', GeneratedContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
