from django.db import models
from django.db.models import CharField, EmailField

# Create your models here.
NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):
    full_name = CharField(max_length=200, verbose_name='ФИО')
    contact_email = EmailField(max_length=254, unique=True, verbose_name='контактный email')
    comment = CharField(max_length=300, verbose_name='комментарий')

    def __str__(self):
        return f'{self.full_name}({self.contact_email}): {self.comment}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
