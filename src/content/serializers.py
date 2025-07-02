from rest_framework import serializers
from .models import Material, FavoriteMaterial, GeneratedContent
from courses.models import Module
from authentication.models import User

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    module = serializers.HyperlinkedRelatedField(
        view_name='module-detail',
        queryset=Module.objects.all()
    )
    favorited_by = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='favoritematerial-detail'
    )

    class Meta:
        model = Material
        fields = [
            'url', 'id', 'module', 'title', 'description',
            'type', 'resource_url', 'text_plain', 'creation_date', 'favorited_by'
        ]
        extra_kwargs = {
            'url': {'view_name': 'material-detail'},
        }


class FavoriteMaterialSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    material = serializers.HyperlinkedRelatedField(
        view_name='material-detail',
        queryset=Material.objects.all()
    )
    
    class Meta:
        model = FavoriteMaterial
        fields = ['url', 'id', 'user', 'material', 'date']
        extra_kwargs = {
            'url': {'view_name': 'favoritematerial-detail'}
        }

class GeneratedContentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    material = serializers.HyperlinkedRelatedField(
        view_name='material-detail',
        queryset=Material.objects.all()
    )

    class Meta:
        model = GeneratedContent
        fields = [
            'url', 'id', 'user', 'material', 'content_type',
            'output_format', 'content', 'creation_date'
        ]
        extra_kwargs = {
            'url': {'view_name': 'generatedcontent-detail'}
        }