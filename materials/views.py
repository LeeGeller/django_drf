from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializer import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ["retrieve", "destroy", "list"]:
            self.permission_classes = [IsAuthenticated, ~IsOwner]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
