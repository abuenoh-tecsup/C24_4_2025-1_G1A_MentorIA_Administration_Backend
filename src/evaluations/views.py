from rest_framework import viewsets
from .models import Evaluation, Question, EvaluationAttempt, QuestionAnswer
from .serializers import EvaluationSerializer, QuestionSerializer, EvaluationAttemptSerializer, QuestionAnswerSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class EvaluationAttemptViewSet(viewsets.ModelViewSet):
    queryset = EvaluationAttempt.objects.all()
    serializer_class = EvaluationAttemptSerializer

class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer