from django.urls import path

from base import views
from base.views import home

urlpatterns = [
    path('', views.home),
    path("send_email/", views.sendEmail, name="send_email"),
    path("", home, name="home")
]
