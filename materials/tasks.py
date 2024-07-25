from django.core.mail import send_mail
from celery import shared_task

from config import settings
from materials.models import Course, Subscription


@shared_task
def send_course_update_notifications(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course)
    for subscription in subscriptions:
        if subscription.user.email:
            send_mail(
                subject="Обновление курса",
                message=f"Курс {course.title} был обновлен.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[subscription.user.email],
            )
