from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name=None, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))
        email = self.normalize_email(email)

        user = self.model(email=email, username=username, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Please assign is_staff=True for superuser'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Please assign is_superuser=True for superuser'))
        return self.create_user(email, username, first_name, password, **other_fields)
