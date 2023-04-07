from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from .managers import CustomAccountManager


# Create your models here.
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(_('User Name'), max_length=150)
    first_name = models.CharField(_('First Name'), max_length=150, null=True)
    last_name = models.CharField(_('Last Name'), max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.email

