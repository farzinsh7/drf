from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
# Create your views here.


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Farzin'}
        )
        message.send(to=['John@gmail.com'])
    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Farzin'})
