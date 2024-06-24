from rest_framework import serializers

from donations.models import Donate
from materials.models import Course


class DonateSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source="course"
    )
    course = serializers.CharField(read_only=True, source="course.title_course")

    class Meta:
        model = Donate
        exclude = ("created_at",)
