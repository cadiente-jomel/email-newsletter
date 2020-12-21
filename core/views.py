from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.

def indexPage(request):

    subject = 'Thank you for registering to our site'
    message = 'it means the world to us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['cadientejomel4@gmail.com']
    try:
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
    except:
        return HttpResponse('there\'s an error sending the message')
    # try:
    #     send_mail(subject, message, email_from, recipient_list, fail_silently=False,)
    #     return HttpResponse('email sent')
    # except:
    #     return HttpResponse('problem encounter')


def subscribePage(request):
    return render(request, 'core/subscribe.html')