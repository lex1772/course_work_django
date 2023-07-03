from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Client(AbstractUser):

    username = None

    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    contact_email = models.EmailField(max_length=254, unique=True, verbose_name='контактный email')
    comment = models.CharField(max_length=255, verbose_name='комментарий', **NULLABLE)
    black_list = models.BooleanField(default=False, verbose_name='черный список')

    USERNAME_FIELD = 'contact_email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.contact_email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    class StatusType(models.Model):
        MANAGER = "MANAGER"
        BASE_USER = "BASE_USER"
        STATUS = [
            (MANAGER, "Manager"),
            (BASE_USER, "Base_user"),
        ]

    status_type = models.CharField(
        max_length=50,
        choices=StatusType.STATUS,
        default=StatusType.BASE_USER,
        verbose_name="роль")
