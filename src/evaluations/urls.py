from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluationViewSet, QuestionViewSet, EvaluationAttemptViewSet, QuestionAnswerViewSet

router = DefaultRouter()
router.register(r'evaluations', EvaluationViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'attempts', EvaluationAttemptViewSet)
router.register(r'answers', QuestionAnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]