from django.shortcuts import render
from django.http import HttpResponse
from .models import Email
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from json import loads
# Create your views here.

def indexPage(request):    
    if request.method == 'POST':
        # try:
        subject = 'You are now subscribed to my weekly newspaper'
        message = 'check out what\'s hot in tech right now'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = list()
        payload = loads(request.body.decode('utf-8'))
        email = payload['email']
        is_exists = Email.objects.filter(email=email).exists()
        if not is_exists:
            new_subscriber = Email.objects.create(email=email)
            new_subscriber.save()
            recipient_list.append(new_subscriber)
            html_content = render_to_string('core/templates.html')
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                subject,
                message,
                email_from,
                recipient_list,
            )
            email.attach_alternative(html_content, 'text/html')
            email.send()
        return HttpResponse('email sent')
        # except:
        #     return HttpResponse('there\'s an error sending the message')

    


  
    # try:
    #     send_mail(subject, message, email_from, recipient_list, fail_silently=False,)
    #     return HttpResponse('email sent')
    # except:
    #     return HttpResponse('problem encounter')


def subscribePage(request):
    return render(request, 'core/subscribe.html')