# Generated by Django 4.2.1 on 2023-07-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0008_mailingtry_mailing_try_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='mailing_status',
            field=models.CharField(choices=[('AC', 'Active'), ('FI', 'Finished'), ('CR', 'Created')], default='CR', max_length=2, verbose_name='статус рассылки'),
        ),
    ]
