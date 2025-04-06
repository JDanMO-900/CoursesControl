from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'area', AreaViewSet)
router.register(r'group', GroupViewSet)
router.register(r'course', CourseViewSet)
router.register(r'personnel', PersonnelViewSet)
router.register(r'course-received', CourseReceivedViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]