from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from .models import Sermon

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages


class SermonView(ListView):
    template_name = 'sermon/sermon.html'
    queryset = Sermon.objects.all()
    paginate_by = 9


class SermonDetailView(DetailView):
    model = Sermon
    template_name = 'sermon/sermon_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']

        post = get_object_or_404(sermon, pk=pk, slug=slug)
        context['post'] = sermon
        return context


class SermonCreateView(LoginRequiredMixin, CreateView):
    model = Sermon
    fields = '__all__'

    def get_success_url(self):
        messages.success(
            self.request, 'Your sermon has been posted successfully.')
        return reverse_lazy("sermon")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


class SermonUpdateView(LoginRequiredMixin, UpdateView):
    model = Sermon
    fields = ["title", "content", "image", "tags"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'This Sermon has been updated successfully.')
        return reverse_lazy("blog")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class SermonDeleteView(LoginRequiredMixin, DeleteView):
    model = Sermon

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("sermon")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
