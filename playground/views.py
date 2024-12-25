from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render

# Create your views here.


def say_hello(request):
    try:
        send_mail('subject', 'message', 'info@drf.com',
                  ['bob@farzinshams.com'])
    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Farzin'})
