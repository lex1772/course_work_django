from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from client.models import Client


class ClientRegisterForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ('contact_email', 'password1', 'password2',)


class ClientProfileForm(UserChangeForm):
    class Meta:
        model = Client
        fields = ('full_name', 'contact_email', )

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
