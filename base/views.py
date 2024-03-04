from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def home(request):
    return render(request, 'base/home.html')


def SendEmail(request):

    if request.method == 'POST':

        template = render_to_string('base/email_template.html', {
            "name": request.POST.get('name'),
            "email": request.POST.get('email'),
            "message": request.POST.get('message')
        })

        email = EmailMessage(request.POST['subject'],
                             template,
                             settings.EMAIL_HOST_USER,
                             ["theandrei.loredana@gmail.com"]
                             )

    email.fail_silently = False
    email.send()
    return HttpResponse("Email was sent!")