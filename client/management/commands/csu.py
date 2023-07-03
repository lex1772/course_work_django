from django.core.management import BaseCommand

from client.models import Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Client.objects.create(
            contact_email="admin@admin.ru",
            first_name="Admin",
            last_name="Admin",
            is_staff=True,
            is_superuser=True
        )

        user.set_password('12345')
        user.save()