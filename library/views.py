from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from .models import Book

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages


class BookView(ListView):
    template_name = 'book/book1.html'
    queryset = Book.objects.all()
    paginate_by = 9


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']

        book = get_object_or_404(Book, pk=pk)
        context['book'] = book
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ["title", "content", "image", "tags"]

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blog")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ["title", "content", "image", "tags"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("blog")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book

    def get_success_url(self):
        messages.success(
            self.request, 'This Book has been deleted successfully.')
        return reverse_lazy("book")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
