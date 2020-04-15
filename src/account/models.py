from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django_countries.fields import CountryField

from django.db import models

from account import model_choices as mch


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    valid_phone = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='it should be: +************')  # нашел в сети
    phone = models.CharField(validators=[valid_phone], max_length=17, null=True, blank=True)

    def __str__(self):
        return f'{self.username}{self.first_name}' \
               f'{self.last_name}{self.bio} {self.birth_date}' \
               f'{self.country} {self.phone}'


class SaveIP(models.Model):
    user = models.CharField(max_length=128, null=True, blank=True)
    user_ip = models.GenericIPAddressField(null=True)
    data_saved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}{self.user_ip}' \
               f'{self.data_saved}'


class SaveSignals(models.Model):
    data_changes = models.DateTimeField(auto_now=True)
    type_changes = models.PositiveSmallIntegerField(choices=mch.TYPE_CHANGES, null=True, blank=True)
    info_changes = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.data_changes}{self.get_type_changes_display()}' \
               f'{self.info_changes}'
