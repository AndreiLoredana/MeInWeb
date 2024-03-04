from django.urls import path

from base import views

urlpatterns = [
    path('', views.home),
    path("send_email/", views.SendEmail, name="send_email")
]
