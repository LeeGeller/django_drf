# Generated by Django 4.2.2 on 2024-06-23 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Donate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(default=0, verbose_name="Сумма"),
                ),
                (
                    "session_id",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Id сессии"
                    ),
                ),
                (
                    "donate_url",
                    models.URLField(
                        blank=True,
                        max_length=400,
                        null=True,
                        verbose_name="Ссылка на оплату",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата курсоа",
                "verbose_name_plural": "Оплата курсов",
            },
        ),
    ]
