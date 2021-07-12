from django import forms
from captcha.fields import CaptchaField

from .models import Contact



class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact

        fields = [
            'first_name',
            'last_name',
            'company_name',
            'email',
            'phone',
            'reason',
            'message',
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre(s)',
                    'required': True,
                    'id': 'first_name'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido(s)',
                    'required': True,
                    'id': 'last_name'
                }
            ),

            'company_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Compañía ó Trabajo',
                    'required': True,
                    'id': 'company_name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                    'required': True,
                    'id': 'email'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'required': True,
                    'id': 'phone'
                }
            ),

            'reason': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Razón de contacto',
                    'required': True,
                    'id': 'reason',
                    'list': 'reasons'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escriba aquí su mensaje...',
                    'required': True,
                    'id': 'message'
                }
            ),
        }
