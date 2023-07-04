# Generated by Django 4.2.1 on 2023-07-04 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0027_mail_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='author',
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]