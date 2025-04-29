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
    area = serializers.CharField()

    class Meta:
        model = Group
        fields = '__all__'

    def get_area(self, obj):
        return obj.area.name if obj.area else None

    def create(self, validated_data):
        area_name = validated_data.pop('area')

        try:
            area = Area.objects.get(name=area_name)
        except Area.DoesNotExist:
            raise serializers.ValidationError({'area': 'Area with this name does not exist.'})

        return Group.objects.create(area=area, **validated_data)

    def update(self, instance, validated_data):
        print("Here:", validated_data)
        print("Here:", self.initial_data)

        area_name = self.initial_data.get('area')

        if area_name:
            try:
                area = Area.objects.get(name=area_name)
                validated_data['area'] = area
            except Area.DoesNotExist:
                raise serializers.ValidationError({'area': 'Area with this name does not exist.'})

        return super().update(instance, validated_data)


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
