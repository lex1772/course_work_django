# Generated by Django 4.2.1 on 2023-07-04 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0022_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingtry',
            name='mailing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings'),
        ),
    ]
