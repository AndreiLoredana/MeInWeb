from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    return render(request, 'base/home.html')


def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('base/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(request.POST['subject'],
                             template,
                             settings.EMAIL_HOST_USER,
                             ["contact@wroom.ro"]
                             )

        email.fail_silently = False
        email.send()

    return render(request, "base/email_sent.html")
