from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('image', 'theme', 'category')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),

        }
