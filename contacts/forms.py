
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'subject'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'message'}),

        }
