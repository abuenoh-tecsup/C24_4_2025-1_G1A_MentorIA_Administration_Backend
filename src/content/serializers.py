from rest_framework import serializers
from .models import Material, FavoriteMaterial
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
        fields = ['url', 'id', 'module', 'title', 'description', 'type', 'url_field', 'creation_date', 'favorited_by']
        extra_kwargs = {
            'url': {'view_name': 'material-detail'},
            'url_field': {'source': 'url'}
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