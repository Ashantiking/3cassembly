from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from .models import Payroll, Status, Maintenance, Charity
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages


# Create your views here.


####################################################################
# PAYROLL SECTION VIEW #
###################################################################

class PayrollView(ListView):
    template_name = 'payroll/payroll.html'
    queryset = Payroll.objects.all()
    paginate_by = 6


class PayrollDetailView(DetailView):
    model = Payroll
    template_name = 'payroll/payroll_detail.html'
    success_url = reverse_lazy('payroll')


class PayrollCreateView(LoginRequiredMixin, CreateView):
    model = Payroll
    fields = ["name", "image", "id_number", "contact", "address", "blood_group",
              "salary", "allowance", "accomodation", "date_employed", "nok_address",
              "nok_contact", "description", "category", "status"
              ]

    def get_success_url(self):
        messages.success(
            self.request, 'Payroll has been created successfully.')
        return reverse_lazy("payroll")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class PayrollUpdateView(LoginRequiredMixin, UpdateView):
    model = Payroll
    fields = ["name", "image", "id_number", "contact", "address", "blood_group",
              "salary", "allowance", "accomodation", "date_employed", "nok_address",
              "nok_contact", "description", "category", "status"
              ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Payroll has been updated successfully.')
        return reverse_lazy("payroll")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class PayrollDeleteView(LoginRequiredMixin, DeleteView):
    model = Payroll

    def get_success_url(self):
        messages.success(
            self.request, 'Payroll has been deleted successfully.')
        return reverse_lazy("payroll")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

####################################################################
        # CHARITY SECTION VIEW #
###################################################################


class CharityView(ListView):
    template_name = 'charity/charity.html'
    queryset = Charity.objects.all()
    paginate_by = 6


class CharityDetailView(DetailView):
    model = Charity
    template_name = 'charity/charity_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']

        Charity = get_object_or_404(Charity, pk=pk)
        context['charity'] = charity
        return context


class CharityCreateView(LoginRequiredMixin, CreateView):
    model = Charity
    fields = ["name", "image", "amount", "description", "category", "status"]

    def get_success_url(self):
        messages.success(
            self.request, 'Charity has been created successfully.')
        return reverse_lazy("charity")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class CharityUpdateView(LoginRequiredMixin, UpdateView):
    model = Charity
    fields = ["name", "image", "amount", "description", "category", "status"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Charity has been updated successfully.')
        return reverse_lazy("charity")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class CharityDeleteView(LoginRequiredMixin, DeleteView):
    model = Charity

    def get_success_url(self):
        messages.success(
            self.request, 'Charity has been deleted successfully.')
        return reverse_lazy("charity")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


####################################################################
        # MAINTENCE SECTION VIEW #
###################################################################


class MaintenanceView(ListView):
    template_name = 'maintenance/maintenance.html'
    queryset = Maintenance.objects.all()
    paginate_by = 6


class MaintenanceDetailView(DetailView):
    model = Maintenance
    template_name = 'maintenance/maintenance_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # since our slug field is not unique, we need the primary key to get a unique post
        pk = self.kwargs['pk']

        Maintenance = get_object_or_404(Maintenance, pk=pk)
        context['maintenance'] = maintenance
        return context


class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    model = Maintenance
    fields = ["amount", "name", "category", "status"]

    def get_success_url(self):
        messages.success(
            self.request, 'Maintenance has been created successfully.')
        return reverse_lazy("maintenance")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class MaintenanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Maintenance
    fields = ["amount", "name", "category", "status"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Maintenance has been updated successfully.')
        return reverse_lazy("maintenance")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class MaintenanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Maintenance

    def get_success_url(self):
        messages.success(
            self.request, 'Maintenance has been deleted successfully.')
        return reverse_lazy("maintenance")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
