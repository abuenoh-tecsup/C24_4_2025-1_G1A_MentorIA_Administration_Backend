from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ForumViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'forums', ForumViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]