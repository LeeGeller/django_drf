from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
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

    def update_course(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from materials.tasks import send_course_update_notifications

        send_course_update_notifications.delay(self.id)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название урока")
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
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, blank=True, null=True
    )
    course = models.ForeignKey(
        "materials.Course", on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user} - {self.course}"
