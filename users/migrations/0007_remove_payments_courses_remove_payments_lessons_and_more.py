# Generated by Django 4.2.2 on 2024-07-23 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0008_alter_subscription_unique_together"),
        ("users", "0006_user_is_subscription"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payments",
            name="courses",
        ),
        migrations.RemoveField(
            model_name="payments",
            name="lessons",
        ),
        migrations.AddField(
            model_name="payments",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="donate_url",
            field=models.URLField(
                blank=True, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="lesson",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.lesson",
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="ID сессии"
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="type_of_payment",
            field=models.CharField(
                choices=[("Курс", "course"), ("Урок", "lesson")],
                max_length=150,
                verbose_name="Тип оплаты",
            ),
        ),
    ]