# Generated by Django 4.2.2 on 2024-07-23 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_payments_courses_remove_payments_lessons_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="date_of_payment",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата оплаты"
            ),
        ),
    ]