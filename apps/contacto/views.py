from django.shortcuts import render
from django import forms
from .models import Contacto
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
# Create your views here.
def mail(request):
    contacto = Contacto.objects.all()[:2]
    email1 = contacto[0].email
    email2 = contacto[1].email
    try:
        datos = request.POST['message']
        email_cliente = request.POST['email']
        subject = request.POST['subject']

    except :
        return  render(request , 'contacto.html')
    else:
        send_mail(subject,
                  datos,
                  email_cliente,
                  [email1,email2],

                  )


