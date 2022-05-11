from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from .models import Faith

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages


class HomeView(ListView):
    template_name = 'blog/index.html'
    queryset = Faith.objects.all()
    paginate_by = 3


class FaithView(ListView):
    template_name = 'faith/faith.html'
    queryset = Faith.objects.all()
    paginate_by = 9


class FaithDetailView(DetailView):
    model = Faith
    template_name = 'faith/faith_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']

        post = get_object_or_404(sermon, pk=pk, slug=slug)
        context['post'] = faith
        return context


class FaithCreateView(LoginRequiredMixin, CreateView):
    model = Faith
    fields = '__all__'

    def get_success_url(self):
        messages.success(
            self.request, 'Your Testamony has been posted successfully.')
        return reverse_lazy("faith")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


class FaithUpdateView(LoginRequiredMixin, UpdateView):
    model = Faith
    fields = ["name", "content", "image"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'This Sermon has been updated successfully.')
        return reverse_lazy("faith")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class FaithDeleteView(LoginRequiredMixin, DeleteView):
    model = Faith

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("faith")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
