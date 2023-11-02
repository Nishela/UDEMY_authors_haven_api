from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password, **kwargs):
        if not first_name:
            raise ValueError(_('Users must have a first name'))
        if not last_name:
            raise ValueError(_('Users must have a last name'))
        if not email:
            raise ValidationError(_('Invalid email address'))

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **kwargs)
        user.set_password(password)

        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)

        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        if not password:
            raise ValueError(_('Superuser must have a password'))

        user = self.create_user(first_name, last_name, email, password, **kwargs)
        user.save(using=self._db)
        return user
