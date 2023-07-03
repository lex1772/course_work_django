from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic

from client import forms
from client.models import Client
from client.tokens import email_verification_token
from config import settings


# Create your views here.
class RegisterView(generic.CreateView):
    model = Client
    form_class = forms.ClientRegisterForm
    template_name = 'client/register.html'
    success_url = reverse_lazy('client:login')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.is_active = False
            client.save()

            current_site = get_current_site(request)
            subject = 'Завершение регистрации'
            message = render_to_string('client/account_activation_email.html', {
                'user': client,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(client.pk)),
                'token': email_verification_token.make_token(client),
            })
            client.email_user(subject, message)

            messages.success(request, ('Пожалуйста подтвердите ваш email для завершения регистрации.'))

        return render(request, self.template_name, {'form': form})


class ProfileView(generic.UpdateView):
    model = Client
    form_class = forms.ClientProfileForm
    success_url = reverse_lazy('client:profile')

    def get_object(self, queryset=None):
        return self.request.user


class ActivateAccount(generic.View):
    success_url = reverse_lazy('client:login')

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Client.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and email_verification_token.check_token(user, token):
            user.is_active = True
            user.email_verify = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('client:profile')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('client:profile')


def generate_new_password(request):
    password = User.objects.make_random_password()
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(password)
    request.user.save()
    return redirect(reverse('client:login'))
