from django.db import models


class Course(models.Model):
    title_course = models.CharField(max_length=200, verbose_name="Название курса")
    preview_course = models.ImageField(
        upload_to="courses/", verbose_name="Превью курса", blank=True, null=True
    )
    description_course = models.TextField(verbose_name="Описание курса")
    created_at_course = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания курса"
    )

    def __str__(self):
        return self.title_course

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title_lesson = models.CharField(max_length=200, verbose_name="Название урока")
    preview_lesson = models.ImageField(
        upload_to="lessons/", verbose_name="Превью урока"
    )
    description_lesson = models.TextField(verbose_name="Описание урока")
    link_to_video = models.URLField(verbose_name="Ссылка на видео")
    created_at_lesson = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания урока"
    )
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_lesson

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
