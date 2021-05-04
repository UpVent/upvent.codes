from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse

from django.conf import settings

from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Captcha Settings
            human = True

            # Email settings
            subject = "Contacto via Sitio Web"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'company_name': form.cleaned_data['company_name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'reason': form.cleaned_data['reason'],
                'message': form.cleaned_data['message']
            }

            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [form.cleaned_data['email']],
                )
                messages.success(request, 'Gracias por ponerse en contacto con\
                nosotros. Responderemos a su mensaje en menos de 12 horas.')

                # Return view
                form.save()
                form = ContactForm
                return render(request, 'contact/contact.html', {'form': form})

            except Exception as e:
                messages.error(request, 'Algo salió mal,\
                tu mensaje no fué enviado.')
                return render(request, 'contact/contact.html', {'form': form})

        else:
            form = ContactForm(request.POST)
            for field in form.errors:
                form.fields[field].widget.attrs['class'] = 'form-control error'
            return render(request, 'contact/contact.html', {'form': form})

    else:
        form = ContactForm
        return render(request, 'contact/contact.html', {'form': form})
