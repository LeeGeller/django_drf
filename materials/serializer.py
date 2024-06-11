from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ("created_at_lesson",)


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source="lesson")

    class Meta:
        model = Course
        exclude = ("created_at_course",)
