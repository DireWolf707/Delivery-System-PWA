from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

USER_MODEL = get_user_model()


@receiver(post_save, sender=USER_MODEL)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        message = f"""
        Hi New User - {instance.get_full_name()}
        Welcome To our website...

        Regards
        """
        send_mail(
            'Welcome To Delivery Service',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )
