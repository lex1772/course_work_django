# Generated by Django 4.2.1 on 2023-07-04 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0019_mail_owner_alter_mail_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mail',
            old_name='client',
            new_name='client_to_message',
        ),
    ]