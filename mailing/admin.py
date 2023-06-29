from django.contrib import admin

from mailing.models import MailingSettings


# Register your models here.
@admin.register(MailingSettings)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('mailing_status', 'mailing_time_start', 'mailing_time_start', 'mailing_periods', )
    list_filter = ('mailing_status',)
    search_fields = ('mailing_status',)