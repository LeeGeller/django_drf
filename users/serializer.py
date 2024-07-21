from rest_framework import serializers

from materials.models import Course
from users.models import Payments, User


class PaymentsSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source="course"
    )
    course = serializers.CharField(read_only=True, source="course.title_course")

    class Meta:
        model = Payments
        exclude = ("created_ad",)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
