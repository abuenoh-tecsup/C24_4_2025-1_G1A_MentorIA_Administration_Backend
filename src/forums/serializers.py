from rest_framework import serializers
from .models import Forum, Comment
from courses.models import Module
from authentication.models import User

class ForumSerializer(serializers.HyperlinkedModelSerializer):
    module = serializers.HyperlinkedRelatedField(
        view_name='module-detail',
        queryset=Module.objects.all()
    )
    author = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )
    
    class Meta:
        model = Forum
        fields = ['url', 'id', 'module', 'author', 'title', 'description', 'creation_date', 'comments']
        extra_kwargs = {
            'url': {'view_name': 'forum-detail'}
        }

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    forum = serializers.HyperlinkedRelatedField(
        view_name='forum-detail',
        queryset=Forum.objects.all()
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    
    class Meta:
        model = Comment
        fields = ['url', 'id', 'forum', 'user', 'content', 'creation_date']
        extra_kwargs = {
            'url': {'view_name': 'comment-detail'}
        }