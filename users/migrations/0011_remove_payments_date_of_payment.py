# Generated by Django 4.2.2 on 2024-07-23 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_alter_payments_session_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payments",
            name="date_of_payment",
        ),
    ]