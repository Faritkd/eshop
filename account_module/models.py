from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه')
    email_activate_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


    def __str__(self):
        return self.get_full_name()