from rest_framework import serializers
from .models import Task, Submission
from courses.models import Module
from authentication.models import User

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    module = serializers.HyperlinkedRelatedField(
        view_name='module-detail',
        queryset=Module.objects.all()
    )
    submissions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='submission-detail'
    )
    
    class Meta:
        model = Task
        fields = ['url', 'id', 'module', 'title', 'description', 'publication_date', 'due_date', 'submissions']
        extra_kwargs = {
            'url': {'view_name': 'task-detail'}
        }

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    task = serializers.HyperlinkedRelatedField(
        view_name='task-detail',
        queryset=Task.objects.all()
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    
    class Meta:
        model = Submission
        fields = ['url', 'id', 'task', 'user', 'submission_date', 'status', 'grade', 'comments', 'file_url']
        extra_kwargs = {
            'url': {'view_name': 'submission-detail'}
        }