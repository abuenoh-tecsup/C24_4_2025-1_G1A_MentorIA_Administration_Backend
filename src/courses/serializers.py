from rest_framework import serializers
from .models import Course, Module, Enrollment, Announcement
from academic.models import Subject, AcademicPeriod
from authentication.models import User, Professor, Student

# serializers.py
class CourseSerializer(serializers.ModelSerializer):
    professor = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all())  # Cambiar a Professor
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    
    class Meta:
        model = Course
        fields = ['id', 'subject', 'professor']

class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    course = serializers.HyperlinkedRelatedField(
        view_name='course-detail',
        queryset=Course.objects.all()
    )
    materials = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='material-detail'
    )
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-detail'
    )
    evaluations = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='evaluation-detail'
    )
    forums = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='forum-detail'
    )
    
    class Meta:
        model = Module
        fields = ['url', 'id', 'course', 'title', 'description', 'module_order', 'materials', 'tasks', 'evaluations', 'forums']
        extra_kwargs = {
            'url': {'view_name': 'module-detail'}
        }

class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(
        view_name='student-detail',
        queryset=Student.objects.all()
    )
    course = serializers.HyperlinkedRelatedField(
        view_name='course-detail',
        queryset=Course.objects.all()
    )
    period = serializers.HyperlinkedRelatedField(
        view_name='academicperiod-detail',
        queryset=AcademicPeriod.objects.all()
    )
    
    class Meta:
        model = Enrollment
        fields = ['url', 'id', 'student', 'course', 'period', 'status', 'enrollment_date']
        extra_kwargs = {
            'url': {'view_name': 'enrollment-detail'}
        }

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    course = serializers.HyperlinkedRelatedField(
        view_name='course-detail',
        queryset=Course.objects.all()
    )
    author = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    
    class Meta:
        model = Announcement
        fields = ['url', 'id', 'course', 'author', 'title', 'content', 'creation_date', 'publication_date']
        extra_kwargs = {
            'url': {'view_name': 'announcement-detail'}
        }
