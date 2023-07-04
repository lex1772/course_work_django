# Generated by Django 4.2.1 on 2023-07-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_rename_client_user'),
        ('mailing', '0023_alter_mailingtry_mailing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='client_to_message',
        ),
        migrations.AddField(
            model_name='mail',
            name='client_to_message',
            field=models.ManyToManyField(blank=True, null=True, to='client.mailingclient', verbose_name='Клиенты'),
        ),
    ]