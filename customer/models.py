from django.db import models
from django.conf import settings


def customer_avatar(instance, filename):
    return f'customer/avatars/{instance.user_id}-{filename}'


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to=customer_avatar, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.get_full_name()
