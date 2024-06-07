from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    preview = models.ImageField(upload_to="courses/", verbose_name="Превью курса")
    description = models.TextField(verbose_name="Описание курса")
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=True, verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
