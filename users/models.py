import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    first_name = models.CharField(verbose_name=_('first name'), max_length=50)
    last_name = models.CharField(verbose_name=_('last name'), max_length=50)
    email = models.EmailField(verbose_name=_('email address'), max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(verbose_name=_('staff status'), default=False)
    is_active = models.BooleanField(verbose_name=_('active'), default=True)

    date_joined = models.DateTimeField(verbose_name=_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.first_name

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    @property
    def get_short_name(self):
        return self.first_name
