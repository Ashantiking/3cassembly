from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'slug', 'image', 'author', 'summary', 'content',
                  'category', 'pdf', 'recommended_books', 'category', 'spiritual_growth_books',
                  'relationship_books', 'empowerment_books', 'movitational_books'
                  )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'summary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Summary'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),


        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'slug', 'image', 'author', 'summary', 'content',
                  'category', 'pdf', 'recommended_books', 'category', 'spiritual_growth_books',
                  'relationship_books', 'empowerment_books', 'movitational_books'
                  )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'summary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Summary'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),


        }
