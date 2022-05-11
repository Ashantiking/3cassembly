from django import forms
from .models import Gallery
from category.models import Category


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image', 'title', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image', 'title', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),

        }
