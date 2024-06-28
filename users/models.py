from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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

    TYPE_OF_PAYMENTS = [("Курс", Course), ("Урок", Lesson)]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="payments",
        blank=True,
        null=True,
    )
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_of_payment = models.DateTimeField(verbose_name="Дата оплаты")

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name="Связь с продуктом"
    )
    product_id = models.PositiveIntegerField(verbose_name="ID продукта")
    product = GenericForeignKey("content_type", "object_id")

    type_of_payment = models.CharField(
        max_length=150,
        verbose_name="Тип оплаты",
        choices=TYPE_OF_PAYMENTS,
    )
    sum_of_payment = models.PositiveIntegerField(verbose_name="Сумма оплаты")

    def __str__(self):
        return f"{self.user}, {self.date_of_payment}, {self.sum_of_payment}"

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
