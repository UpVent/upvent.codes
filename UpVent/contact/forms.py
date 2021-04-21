from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        fields = [
            'first_name',
            'last_name',
            'company_name',
            'email',
            'phone',
            'reason',
            'message'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'autocomplete', 'id': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'autocomplete', 'id': 'last_name'}),
            'company_name': forms.TextInput(attrs={'class': 'autocomplete', 'id': 'company_name'}),
            'email': forms.EmailInput(attrs={'class': 'autocomplete', 'id': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'autocomplete', 'id': 'company_name'}),
            'reason': forms.TextInput(attrs={'class': 'autocomplete', 'id': 'first_name'}),
            'message': forms.Textarea(attrs={'class': 'autocomplete', 'id': 'first_name'}),
        }
