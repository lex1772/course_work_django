# Generated by Django 4.2.1 on 2023-07-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0026_rename_user_mail_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активный'),
        ),
    ]