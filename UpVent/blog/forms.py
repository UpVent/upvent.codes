from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = [
            'name',
            'email',
            'website',
            'body',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre Completo o Apodo',
                    'required': True,
                    'id': 'name'
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

            'website': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Sitio Web (Opcional)',
                    'id': 'website'
                }
            ),

            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribir comentario...',
                    'required': True,
                    'id': 'body'
                }
            ),
        }
