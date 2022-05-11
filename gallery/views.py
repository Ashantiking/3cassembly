
from django.db import models
from django.shortcuts import render,  get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Gallery
from .forms import GalleryForm, EditForm
from django.http import HttpResponseRedirect
# Create your views here.



class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    ordering = ['-publication_date']


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery/gallery_details.html'
    success_url = reverse_lazy('gallery_details')

    def get_context_data(self, *args, **kwargs):
        #        cat_menu = Category.objects.all()
        context = super(GalleryDetailView, self).get_context_data()

        stuff = get_object_or_404(Gallery, id=self.kwargs['pk'])
        #total_likes = stuff.total_likes()
        #context["cat_menu"] = cat_menu
        #context["total_likes"] = total_likes
        return context


class AddGalleryView(CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = 'gallery/add_gallery.html'
    success_url = reverse_lazy('gallery')



class UpdateGalleryView(UpdateView):
    model = Gallery
    form_class = EditForm
    template_name = 'gallery/update_gallery.html'
    success_url = reverse_lazy('gallery')


class DeleteGalleryView(DeleteView):
    model = Gallery
    template_name = 'gallery/delete_gallery.html'
    success_url = reverse_lazy('gallery')
