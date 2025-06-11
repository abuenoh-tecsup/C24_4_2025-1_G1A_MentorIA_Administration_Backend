from rest_framework import serializers
from .models import Career, Subject, AcademicPeriod

class CareerSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='student-detail'
    )
    
    class Meta:
        model = Career
        fields = ['url', 'id', 'code', 'name', 'students']
        extra_kwargs = {
            'url': {'view_name': 'career-detail'}
        }

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='course-detail'
    )
    
    class Meta:
        model = Subject
        fields = ['url', 'id', 'name', 'courses']
        extra_kwargs = {
            'url': {'view_name': 'subject-detail'}
        }

class AcademicPeriodSerializer(serializers.HyperlinkedModelSerializer):
    enrollments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='enrollment-detail'
    )
    
    class Meta:
        model = AcademicPeriod
        fields = ['url', 'id', 'name', 'year', 'term', 'start_date', 'end_date', 'enrollments']
        extra_kwargs = {
            'url': {'view_name': 'academicperiod-detail'}
        }