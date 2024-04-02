from ..models import Course, Enrollment

from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        
        return Course.objects.create(**validated_data)
    

class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = '__all__'

    def create(self, validated_data):
        
        return Enrollment.objects.create(**validated_data)
    

    