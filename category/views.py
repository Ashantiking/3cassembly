
from django.db import models
from django.shortcuts import render,  get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category
from .forms import CategoryForm, EditForm
from django.http import HttpResponseRedirect
# Create your views here.


class CategoryView(ListView):
    model = Category
    template_name = 'category/category.html'
    ordering = ['-publication_date']
    success_url = reverse_lazy('category')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_details.html'
    success_url = reverse_lazy('category_details')

    def get_context_data(self, *args, **kwargs):
        #        cat_menu = Category.objects.all()
        context = super(CategoryDetailView, self).get_context_data()

        stuff = get_object_or_404(Category, id=self.kwargs['pk'])
        #total_likes = stuff.total_likes()
        #context["cat_menu"] = cat_menu
        #context["total_likes"] = total_likes
        return context


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/add_category.html'
    success_url = reverse_lazy('event')

# class AddCategoryView(CreateView):
#    model = Category
    #form_class = PostForm
#    template_name = 'add_category.html'
#    fields = '__all__'


class UpdateCategoryView(UpdateView):
    model = Category
    form_class = EditForm
    template_name = 'category/update_category.html'
    success_url = reverse_lazy('category')


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'category/delete_category.html'
    success_url = reverse_lazy('category')
