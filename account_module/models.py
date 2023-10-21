from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    avatar = models.CharField(max_length=20, verbose_name='تصویر آواتار', null=True, blank=True)
    email_activate_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email