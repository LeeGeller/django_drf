# Generated by Django 4.2.2 on 2024-06-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_payments_cash_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="Активирован"),
        ),
    ]