from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    age = models.PositiveIntegerField(_('age'))
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
