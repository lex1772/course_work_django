from datetime import datetime

from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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

    #def get_object(self, queryset=None):
        #self.object = super().get_object(queryset)
        #if self.object.author != self.request.user and not self.request.user.status_type == 'MODERATOR':
            #raise PermissionDenied
        #return self.object


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MailFormset = inlineformset_factory(models.MailingSettings, models.Mail, form=forms.MailForm, can_delete=False, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = MailFormset(self.request.POST or None, instance=self.object)
            #print(context_data['formset'])
            if context_data['formset'].is_valid():
                print('formset valid')
            else:
                # Formset is invalid, process forms individually
                for form in context_data['formset']:
                    if form.is_valid():
                        print('form valid')
                    else:
                        print('form invalid')
        else:
            context_data['formset'] = MailFormset(instance=self.object)


        return context_data

    def form_valid(self, form):
        data = self.get_context_data()
        formset = data['formset']
        print(formset)
        for fo in formset:
            print("fo")
            if fo.is_valid():
                print("form valid")
                print(fo.cleaned_data.get("client"))
        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.mailing_status = "AC"
            mailing.save()
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    #def post(self, request, *args, **kwargs):
        #form = self.form_class(request.POST)
        #context = super().get_context_data(**kwargs)
        #if form.is_valid():
            #mailing = form.save(commit=False)
            #mail_data = models.Mail.objects.get(id=mailing.id)
            #print(mail_data)

            #formset = data['formset']
            #for set in formset:
                #if set.is_valid():
                    #print('fc_d', set.cleaned_data)
            #mailing.mailing_status = "AC"
            #mailing.save()
            #if mailing.mailing_time_start < datetime.now() < mailing.mailing_time_end:
                #message = (mailing.mailing_subject, mailing.mailing_body, 'lexa17721@yandex.ru', *)
        #return HttpResponseRedirect(reverse_lazy('mailing:homepage'))
