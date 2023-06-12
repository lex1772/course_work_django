from django.contrib import admin

from client.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'contact_email', 'comment', )
    list_filter = ('full_name', 'contact_email', 'comment', )