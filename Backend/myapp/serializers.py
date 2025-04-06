from rest_framework import serializers
from .models import *

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

    def validate_name(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("El nombre no puede tener más de 50 caracteres.")
        return value

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class PersonnelSerializar(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'

class CourseReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReceived
        fields = '__all__'