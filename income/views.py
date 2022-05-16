from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from .models import Income
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages


# Create your views here.


####################################################################
# INCOME SECTION VIEW #
###################################################################


class IncomeView(ListView):
    template_name = 'payroll/income.html'
    queryset = Income.objects.all()
    paginate_by = 10


class IncomeDetailView(DetailView):
    model = Income
    template_name = 'payroll/income_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']

        income = get_object_or_404(Income, pk=pk)
        context['income'] = Income
        return context


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    fields = ["name", "item", "quantity", "unit_price"]

    def get_success_url(self):
        messages.success(
            self.request, 'Income has been created successfully.')
        return reverse_lazy("income")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    fields = ["name", "item", "quantity", "unit_price"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Income has been updated successfully.')
        return reverse_lazy("income")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income

    def get_success_url(self):
        messages.success(
            self.request, 'Income has been deleted successfully.')
        return reverse_lazy("income")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
