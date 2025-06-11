from rest_framework import serializers
from .models import Evaluation, Question, EvaluationAttempt, QuestionAnswer
from courses.models import Module
from authentication.models import User

class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
    module = serializers.HyperlinkedRelatedField(
        view_name='module-detail',
        queryset=Module.objects.all()
    )
    questions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='question-detail'
    )
    attempts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='evaluationattempt-detail'
    )
    
    class Meta:
        model = Evaluation
        fields = ['url', 'id', 'module', 'title', 'description', 'start_date', 'end_date', 'time_limit', 'questions', 'attempts']
        extra_kwargs = {
            'url': {'view_name': 'evaluation-detail'}
        }

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    evaluation = serializers.HyperlinkedRelatedField(
        view_name='evaluation-detail',
        queryset=Evaluation.objects.all()
    )
    answers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='questionanswer-detail'
    )
    
    class Meta:
        model = Question
        fields = ['url', 'id', 'evaluation', 'statement', 'type', 'options', 'correct_answer', 'answers']
        extra_kwargs = {
            'url': {'view_name': 'question-detail'}
        }

class EvaluationAttemptSerializer(serializers.HyperlinkedModelSerializer):
    evaluation = serializers.HyperlinkedRelatedField(
        view_name='evaluation-detail',
        queryset=Evaluation.objects.all()
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    answers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='questionanswer-detail'
    )
    
    class Meta:
        model = EvaluationAttempt
        fields = ['url', 'id', 'evaluation', 'user', 'submission_date', 'status', 'score', 'comments', 'answers']
        extra_kwargs = {
            'url': {'view_name': 'evaluationattempt-detail'}
        }

class QuestionAnswerSerializer(serializers.HyperlinkedModelSerializer):
    attempt = serializers.HyperlinkedRelatedField(
        view_name='evaluationattempt-detail',
        queryset=EvaluationAttempt.objects.all()
    )
    question = serializers.HyperlinkedRelatedField(
        view_name='question-detail',
        queryset=Question.objects.all()
    )
    
    class Meta:
        model = QuestionAnswer
        fields = ['url', 'id', 'attempt', 'question', 'answer', 'correct']
        extra_kwargs = {
            'url': {'view_name': 'questionanswer-detail'}
        }