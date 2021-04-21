from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
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
                    'admin@example.com',
                    ['admin@example.com']
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found')


            # Return view
            form = ContactForm
            form.save()
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = ContactForm
        return render(request, 'contact/contact.html', {'form': form})
