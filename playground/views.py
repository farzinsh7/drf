from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render

# Create your views here.


def say_hello(request):
    try:
        message = EmailMessage('subject', 'message',
                               'info@attach.com', ['john@gmail.com'])
        message.attach_file('playground/static/images/contact.webp')
        message.send()
    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Farzin'})
