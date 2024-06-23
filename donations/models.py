from django.db import models

from materials.models import Course
from users.models import User


class Donate(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.PositiveIntegerField(default=0, verbose_name="Сумма")
    session_id = models.CharField(
        max_length=200, verbose_name="Id сессии", blank=True, null=True
    )
    donate_url = models.URLField(
        max_length=400, verbose_name="Ссылка на оплату", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Оплата курсоа"
        verbose_name_plural = "Оплата курсов"
