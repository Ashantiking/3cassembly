from category.models import Category
from .models import Sermon
from django import forms


class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ('theme', 'preached_by', 'author', 'description', 'videofile', 'image', 'category',
                  'language', 'status', 'views_count'
                  )

        widgets = {
            'theme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'preached_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'videofile': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'image': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'language': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),


        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ('theme', 'preached_by', 'author', 'description', 'videofile', 'image', 'category',
                  'language', 'status', 'views_count'
                  )

        widgets = {
            'theme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'preached_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'videofile': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'image': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'language': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),


        }
