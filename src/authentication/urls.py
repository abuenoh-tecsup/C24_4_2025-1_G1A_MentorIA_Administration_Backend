from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfessorViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'professors', ProfessorViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]