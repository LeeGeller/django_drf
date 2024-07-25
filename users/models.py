from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = PhoneNumberField(unique=True, verbose_name="Телефон", blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name="Город")
    avatar = models.ImageField(
        upload_to="users/", blank=True, null=True, verbose_name="Аватар"
    )
    is_active = models.BooleanField(default=False, verbose_name="Активирован")
    is_subscription = models.BooleanField(default=False, verbose_name="Подписка")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    TYPE_OF_PAYMENTS = [("Наличные", "cash"), ("Карта", "card")]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="payments",
        blank=True,
        null=True,
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)

    type_of_payment = models.CharField(
        max_length=150,
        verbose_name="Тип оплаты",
        choices=TYPE_OF_PAYMENTS,
    )
    sum_of_payment = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    donate_url = models.TextField(
        verbose_name="Ссылка на оплату", blank=True, null=True
    )
    session_id = models.TextField(verbose_name="ID сессии", blank=True, null=True)

    def __str__(self):
        return f"{self.user}, {self.sum_of_payment}"

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
