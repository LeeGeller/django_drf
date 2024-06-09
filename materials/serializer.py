from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ("created_at_course",)


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ("created_at_lesson",)
