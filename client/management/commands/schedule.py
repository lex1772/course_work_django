from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.core.management import BaseCommand

from client.models import MailingClient
from config import settings
from mailing.models import Mail, MailingSettings, MailingTry


class Command(BaseCommand):

    def handle(self, *args, **options):
        for mail in Mail.objects.values():
            setting = MailingSettings.objects.get(id=mail["settings_id"])
            client = MailingClient.objects.get(id=mail["client_to_message_id"])
            if setting.mailing_status == "AC":
                setting.mailing_time_start = datetime.now()
                sending = send_mail(mail["mailing_subject"], mail["mailing_body"], settings.DEFAULT_FROM_EMAIL,
                                    recipient_list=[client.contact_email],
                                    fail_silently=False)
                if sending == 1:
                    setting.mail_status = 'OK'
                else:
                    setting.mail_status = 'Не отправлено'

                if (setting.mailing_periods == "DL") and ((
                                                                      setting.mailing_time_end - setting.mailing_time_start) <= timedelta(
                    days=1)):
                    setting.mailing_status = 'FI'
                    setting.save()
                elif (setting.mailing_periods == "WL") and ((
                                                                        setting.mailing_time_end - setting.mailing_time_start) <= timedelta(
                    days=6)):
                    setting.mailing_status = 'FI'
                    setting.save()
                elif (setting.mailing_periods == "ML") and ((
                                                                        setting.mailing_time_end - setting.mailing_time_start) <= timedelta(
                    days=30)):
                    setting.mailing_status = 'FI'
                    setting.save()

                MailingTry.objects.create(mailing=setting, mailing_try=datetime.now(),
                                                 mailing_try_status=setting.mailing_status,
                                                 mailing_response=setting.mail_status)

