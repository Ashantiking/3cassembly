from django import forms
from .models import Event
from category.models import Category


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('image', 'theme', 'category')

        widgets = {
            'theme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Theme'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('image', 'theme', 'category')

        widgets = {
            'theme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Theme'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),

        }
