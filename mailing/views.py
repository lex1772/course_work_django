from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.forms import inlineformset_factory

from django.urls import reverse_lazy
from django.views import generic

from config import settings
from mailing import models, forms


# Create your views here.
class HomePage(generic.TemplateView):
    template_name = "home_page.html"


class MailingCreateView(generic.CreateView):
    template_name = "mailing\mail_form.html"
    model = models.MailingSettings
    form_class = forms.SettingsForm
    success_url = reverse_lazy('mailing:homepage')
    mail_data = ''
    mail_status = 'OK'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MailFormset = inlineformset_factory(models.MailingSettings, models.Mail, form=forms.MailForm, can_delete=False,
                                            extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = MailFormset(self.request.POST or None, instance=self.object)
        else:
            context_data['formset'] = MailFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        data = self.get_context_data()
        self.object = form.save()
        formset = data['formset']
        client_email = ''
        mailing_subject = ''
        mailing_body = ''
        for fo in formset:
            if fo.is_valid():
                client_email = fo.cleaned_data.get('client')
                mailing_subject = fo.cleaned_data.get('mailing_subject')
                mailing_body = fo.cleaned_data.get('mailing_body')
                all_clients = fo.cleaned_data.get('all_clients')
                if all_clients:
                    client_email = list(models.Client.objects.all().values_list('contact_email', flat=True))
        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.mailing_status = "AC"
            mailing.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        self.object.save()
        ct = datetime.now()

        if self.object.mailing_time_start.timestamp() <= ct.timestamp() <= self.object.mailing_time_end.timestamp():
            sending = send_mail(mailing_subject, mailing_body, settings.DEFAULT_FROM_EMAIL,
                                recipient_list=[client_email],
                                fail_silently=False)
            print('письмо ушло')
            if sending == 1:
                self.mail_status = 'OK'
            else:
                self.mail_status = 'Не отправлено'

        if (self.object.mailing_periods == "DL") and ((
                                                              self.object.mailing_time_end - self.object.mailing_time_start) <= timedelta(
            days=1)):
            self.object.mailing_status = 'FI'
            self.object.save()
        elif (self.object.mailing_periods == "WL") and ((
                                                                self.object.mailing_time_end - self.object.mailing_time_start) <= timedelta(
            days=6)):
            self.object.mailing_status = 'FI'
            self.object.save()
        elif (self.object.mailing_periods == "ML") and ((
                                                                self.object.mailing_time_end - self.object.mailing_time_start) <= timedelta(
            days=30)):
            self.object.mailing_status = 'FI'
            self.object.save()

        models.MailingTry.objects.create(mailing=self.object, mailing_try=datetime.now(),
                                         mailing_try_status=self.object.mailing_status,
                                         mailing_response=self.mail_status)
        return super().form_valid(form)
