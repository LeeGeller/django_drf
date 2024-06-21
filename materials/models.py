from django.db import models


class Course(models.Model):
    title_course = models.CharField(max_length=200, verbose_name="Название курса")
    preview_course = models.ImageField(
        upload_to="courses/", verbose_name="Превью курса", blank=True, null=True
    )
    description_course = models.TextField(verbose_name="Описание курса")
    link_to_video_course = models.URLField(
        verbose_name="Ссылка на видео курса", blank=True, null=True
    )
    created_at_course = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания курса"
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="course_owner",
    )

    def __str__(self):
        return self.title_course

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title_lesson = models.CharField(max_length=200, verbose_name="Название урока")
    preview_lesson = models.ImageField(
        upload_to="lessons/", verbose_name="Превью урока", blank=True, null=True
    )
    description_lesson = models.TextField(verbose_name="Описание урока")
    link_to_video_lesson = models.URLField(
        verbose_name="Ссылка на видео урока", blank=True, null=True
    )
    created_at_lesson = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания урока"
    )
    lessons = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", blank=True, null=True
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="lesson_owner",
    )

    def __str__(self):
        return self.title_lesson

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    course = models.ForeignKey("materials.Course", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
