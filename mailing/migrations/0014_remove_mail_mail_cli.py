# Generated by Django 4.2.1 on 2023-07-04 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0013_mail_mail_cli_alter_mail_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='mail_cli',
        ),
    ]
