from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]