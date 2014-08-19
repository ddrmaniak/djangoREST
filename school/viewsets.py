from rest_framework import viewsets
from school.models import Teacher, Student
from school.serializers import TeacherSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]