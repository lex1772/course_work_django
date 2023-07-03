from django import forms
from django.db import models
from datetime import datetime

from client.models import NULLABLE, Client


class Status(models.TextChoices):
    ACTIVE = 'AC', 'Active'
    FINISHED = 'FI', 'Finished'
    CREATED = 'CR', 'Created'


class Periods(models.TextChoices):
    DAILY = 'DL', 'Daily'
    WEEKLY = 'WL', 'Weekly'
    MONTHLY = 'ML', 'Monthly'


class MailingSettings(models.Model):
    mailing_status = models.CharField(max_length=2, choices=Status.choices, default=Status.CREATED,
                                      verbose_name='статус рассылки')
    mailing_time_start = models.DateTimeField(verbose_name='время начала рассылки', **NULLABLE)
    mailing_time_end = models.DateTimeField(verbose_name='время конца рассылки', **NULLABLE)
    mailing_periods = models.CharField(max_length=2, choices=Periods.choices, verbose_name='периодичность')

    def __str__(self):
        return f'{self.mailing_status}({self.mailing_time_start}), {self.mailing_periods}'

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылки'


class Mail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE)
    settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE)
    mailing_subject = models.CharField(max_length=255, verbose_name='тема письма')
    mailing_body = models.CharField(max_length=500, verbose_name='тело письма')
    all_clients = models.BooleanField(verbose_name='все клиенты', **NULLABLE)

    def __str__(self):
        return f'{self.mailing_subject}: {self.mailing_body}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailingTry(models.Model):
    mailing = models.ForeignKey(MailingSettings, on_delete=models.DO_NOTHING)
    mailing_try = models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')
    mailing_try_status = models.CharField(max_length=255, verbose_name='статус рассылки', **NULLABLE)
    mailing_response = models.CharField(max_length=255, verbose_name='ответ почтового сервера', **NULLABLE)

    def __str__(self):
        return f'{self.mailing_try.strftime("%d.%m.%Y %H:%M")} ({self.mailing_try_status}): {self.mailing_response}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
