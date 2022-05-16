
####################################################################
# PAYROLL SECTION URLS #
###################################################################

from django.urls import path
from .views import PayrollView,  PayrollDetailView,  PayrollCreateView,  PayrollUpdateView,  PayrollDeleteView, CharityView, CharityDetailView, CharityCreateView, CharityUpdateView, CharityDeleteView, MaintenanceView, MaintenanceDetailView, MaintenanceCreateView, MaintenanceUpdateView, MaintenanceDeleteView, ProcurementView, ProcurementDetailView, ProcurementCreateView, ProcurementUpdateView, ProcurementDeleteView


urlpatterns = [
    path('',  PayrollView.as_view(), name='payroll'),
    path('payroll/<int:pk>/',  PayrollDetailView.as_view(), name='payroll_details'),
    path('payroll/create/',  PayrollCreateView.as_view(), name=' payroll_create'),
    path('payroll/<int:pk>/',  PayrollUpdateView.as_view(), name='payroll_update'),
    path('payroll/<int:pk>/delete/',
         PayrollDeleteView.as_view(), name='payroll_delete'),
    path('charity/',  CharityView.as_view(), name='charity'),
    path('charity/<int:pk>/',  CharityDetailView.as_view(), name='charity_detail'),
    path('charity/create/',  CharityCreateView.as_view(), name='charity_create'),
    path('charity/<int:pk>/',  CharityUpdateView.as_view(), name='charity_update'),
    path('charity/<int:pk>/delete/',
         CharityDeleteView.as_view(), name='charity_delete'),
    path('maintenance/',  MaintenanceView.as_view(), name='maintenance'),
    path('maintenance/<int:pk>/',  MaintenanceDetailView.as_view(),
         name='maintenance_detail'),
    path('maintenance/create/',  MaintenanceCreateView.as_view(),
         name='maintenance_create'),
    path('maintenance/<int:pk>/',  MaintenanceUpdateView.as_view(),
         name='maintenance_update'),
    path('maintenance/<int:pk>/delete/',
         MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('procurement/',  ProcurementView.as_view(), name='procurement'),
    path('procurement/<int:pk>/',  ProcurementDetailView.as_view(),
         name='procurement_details'),
    path('procurement/create/',  ProcurementCreateView.as_view(),
         name='procurement_create'),
    path('procurement/<int:pk>/',  ProcurementUpdateView.as_view(),
         name='procurement_update'),
    path('procurement/<int:pk>/delete/',
         ProcurementDeleteView.as_view(), name='procurement_delete'),


]
