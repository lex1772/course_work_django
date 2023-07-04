# Generated by Django 4.2.1 on 2023-07-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_client_black_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('contact_email', models.EmailField(max_length=254, unique=True, verbose_name='контактный email')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='комментарий')),
            ],
        ),
    ]
