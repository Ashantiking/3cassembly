from category.models import Category
from .models import Faith
from django import forms


class FaithForm(forms.ModelForm):
    class Meta:
        model = Faith
        fields = ('name', 'video', 'content', 'description', 'image', 'category',

                  )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'video': forms.Select(attrs={'class': 'form-control', 'placeholder': 'video'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'content'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Faith
        fields = ('name', 'video', 'content', 'description', 'image', 'category',

                  )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'video': forms.Select(attrs={'class': 'form-control', 'placeholder': 'video'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'content'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
        }
