from django.urls import path

from mailing import views
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path('', views.HomePage.as_view(template_name='mailing/home_page.html'), name='homepage'),
    path('create/', views.MailingCreateView.as_view(), name='create'),
]
