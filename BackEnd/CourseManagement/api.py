from rest_framework.decorators import permission_classes
from .models import Course
from rest_framework import viewsets, permissions
from .serializers import CourseSerializers

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseSerializers