from django import forms

from client.models import Client
from mailing import models


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailForm(StyleFormMixin, forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=False)

    class Meta:
        model = models.Mail
        fields = ('mailing_subject', 'mailing_body', 'client', 'all_clients')




class SettingsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = models.MailingSettings
        fields = ('mailing_time_start', 'mailing_time_end', 'mailing_periods',)
        widgets = {
            'mailing_time_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'mailing_time_end': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
