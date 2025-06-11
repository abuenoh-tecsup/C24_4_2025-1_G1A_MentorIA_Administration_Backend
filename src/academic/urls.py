from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CareerViewSet, SubjectViewSet, AcademicPeriodViewSet

router = DefaultRouter()
router.register(r'careers', CareerViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'periods', AcademicPeriodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]