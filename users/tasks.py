from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone


@shared_task
def block_inactive_users():
    User = get_user_model()
    threshold_date = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=threshold_date, is_active=True)
    for user in inactive_users:
        user.is_active = False
        user.save()
