# Generated by Django 4.2.2 on 2024-06-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_course_preview_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="preview_lesson",
            field=models.ImageField(
                blank=True, null=True, upload_to="lessons/", verbose_name="Превью урока"
            ),
        ),
    ]