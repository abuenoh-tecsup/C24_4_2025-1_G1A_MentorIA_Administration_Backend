from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Professor, Student
from academic.models import Career

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    professor_profile = serializers.HyperlinkedRelatedField(
        view_name='professor-detail',
        read_only=True,
        allow_null=True
    )
    student_profile = serializers.HyperlinkedRelatedField(
        view_name='student-detail',
        read_only=True,
        allow_null=True
    )
    
    class Meta:
        model = User
        fields = [
            'url', 'id', 'username', 'email', 'phone', 'first_name', 
            'last_name', 'date_joined', 'last_login', 'profile_picture_url', 
            'role', 'password', 'professor_profile', 'student_profile'
        ]
        extra_kwargs = {
            'url': {'view_name': 'user-detail'},
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    user_details = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Professor
        fields = [
            'url', 'id', 'user', 'user_details', 'employee_code', 
            'hire_date', 'department', 'academic_title', 
            'office_location', 'status'
        ]
        extra_kwargs = {
            'url': {'view_name': 'professor-detail'}
        }

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    career = serializers.HyperlinkedRelatedField(
        view_name='career-detail',
        queryset=Career.objects.all()
    )
    user_details = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Student
        fields = [
            'url', 'id', 'user', 'user_details', 'career', 'student_code',
            'enrollment_date', 'current_semester', 'average_grade', 'status'
        ]
        extra_kwargs = {
            'url': {'view_name': 'student-detail'}
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User account is disabled.')
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include username and password.')
        
        return data