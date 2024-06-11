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
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="payments",
        blank=True,
        null=True,
    )
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_of_payment = models.DateField(
        verbose_name="Дата оплаты", blank=True, null=True
    )
    courses = models.ForeignKey(
        Course,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="payment_courses",
    )
    lessons = models.ForeignKey(
        Lesson,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="payment_lessons",
    )
    sum_of_payment = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    cash = models.BooleanField(
        verbose_name="Наличные", default=False, blank=True, null=True
    )
    transfer_to_account = models.BooleanField(
        verbose_name="Перевод на счет", default=False, blank=True, null=True
    )

    def __str__(self):
        return (
            f"{self.user}, {self.date_of_payment}, {self.sum_of_payment}, {self.cash}, "
            f"{self.transfer_to_account}, {self.courses}, {self.lessons}"
        )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
