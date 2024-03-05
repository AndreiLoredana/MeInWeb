from django.urls import path

from base import views

urlpatterns = [
    path('', views.home),
    path("send_email/", views.sendEmail, name="send_email")
]
