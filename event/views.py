
from django.db import models
from django.shortcuts import render,  get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event
from .forms import EventForm, EditForm
from django.http import HttpResponseRedirect
# Create your views here.


class EventView(ListView):
    model = Event
    template_name = 'events/event.html'
    ordering = ['-publication_date']
    success_url = reverse_lazy('event')


class EventDetailView(DetailView):
    model = Event
    template_name = 'gallery/event_details.html'
    success_url = reverse_lazy('event_details')

    def get_context_data(self, *args, **kwargs):
        #        cat_menu = Category.objects.all()
        context = super(EventDetailView, self).get_context_data()

        stuff = get_object_or_404(Event, id=self.kwargs['pk'])
        #total_likes = stuff.total_likes()
        #context["cat_menu"] = cat_menu
        #context["total_likes"] = total_likes
        return context


class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'gallery/add_event.html'
    success_url = reverse_lazy('event')

# class AddCategoryView(CreateView):
#    model = Category
    #form_class = PostForm
#    template_name = 'add_category.html'
#    fields = '__all__'


class UpdateEventView(UpdateView):
    model = Event
    form_class = EditForm
    template_name = 'gallery/update_event.html'
    success_url = reverse_lazy('gallery')


class DeleteEventView(DeleteView):
    model = Event
    template_name = 'gallery/delete_event.html'
    success_url = reverse_lazy('event')
