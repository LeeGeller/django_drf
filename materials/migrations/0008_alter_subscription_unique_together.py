# Generated by Django 4.2.2 on 2024-06-21 11:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("materials", "0007_subscription"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="subscription",
            unique_together={("user", "course")},
        ),
    ]
