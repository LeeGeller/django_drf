from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title_course",
        "preview_course",
        "description_course",
        "created_at_course",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "title_lesson",
        "preview_lesson",
        "description_lesson",
        "created_at_lesson",
    )
