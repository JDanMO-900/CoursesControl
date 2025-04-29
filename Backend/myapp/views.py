from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status


# Create your views here.
class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all().filter(delete_at=False).order_by('-created_at')
    serializer_class = AreaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete_at = True
        instance.save()
        return Response(status=204)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().filter(delete_at=False).order_by('-created_at')
    serializer_class = GroupSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete_at = True
        instance.save()
        return Response(status=204)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().filter(delete_at=False).order_by('-created_at')
    serializer_class = CourseSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete_at = True
        instance.save()
        return Response(status=204)


class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all().filter(delete_at=False).order_by('-created_at')
    serializer_class = PersonnelSerializar

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete_at = True
        instance.save()
        return Response(status=204)


class CourseReceivedViewSet(viewsets.ModelViewSet):
    queryset = CourseReceived.objects.all().filter(delete_at=False).order_by('-created_at')
    serializer_class = CourseReceivedSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete_at = True
        instance.save()
        return Response(status=204)
