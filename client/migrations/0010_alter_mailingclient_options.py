# Generated by Django 4.2.1 on 2023-07-04 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_mailingclient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingclient',
            options={'verbose_name': 'Клиент для рассылки', 'verbose_name_plural': 'Клиенты для рассылки'},
        ),
    ]