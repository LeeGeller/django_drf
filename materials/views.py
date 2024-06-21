from rest_framework import generics, viewsets
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.paginators import CoursesPaginator
from materials.serializer import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("pk")
    serializer_class = CourseSerializer
    pagination_class = CoursesPaginator

    def get_permissions(self):
        if self.action in ["retrieve", "destroy", "update"]:
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ["create", "list"]:
            self.permission_classes = [IsAuthenticated, IsModerator]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        request.data["owner"] = request.user.id
        return super().create(request, *args, **kwargs)


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CoursesPaginator


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )


class SubscriptionAPIView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsOwner,
        IsModerator,
    )

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get("course")
        course_item = get_object_or_404(Course, id=course_id)

        subscription_exists = Subscription.objects.filter(
            user=user, course=course_item
        ).exists()

        if subscription_exists:
            Subscription.objects.filter(user=user, course=course_item).delete()
            message = "Вы отписались от курса"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "Вы подписались на курс"
        return Response({"message": message})
