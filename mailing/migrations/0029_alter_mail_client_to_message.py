# Generated by Django 4.2.1 on 2023-07-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0017_remove_user_contact_email_alter_user_email'),
        ('mailing', '0028_remove_mail_author_mailingsettings_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='client_to_message',
            field=models.ManyToManyField(blank=True, null=True, related_name='client_to_message', to='client.mailingclient', verbose_name='Клиенты'),
        ),
    ]