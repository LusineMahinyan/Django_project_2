from celery import shared_task
from django.core.mail import send_mail

from .models import Subscription


@shared_task
def send_course_update_email(course_id):
    subscriptions = Subscription.objects.filter(
        course_id=course_id
    ).select_related("user", "course")

    emails = [
        subscription.user.email
        for subscription in subscriptions
        if subscription.user.email
    ]

    if emails:
        send_mail(
            subject="Обновление курса",
            message="Материалы курса были обновлены.",
            from_email=None,
            recipient_list=emails,
            fail_silently=False,
        )
