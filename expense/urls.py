
####################################################################
# PAYROLL SECTION URLS #
###################################################################

from django.urls import path
from .views import PayrollView,  PayrollDetailView,  PayrollCreateView,  PayrollUpdateView,  PayrollDeleteView


urlpatterns = [
    path('',  PayrollView.as_view(), name='Payroll'),
    path('payroll/<int:pk>/',  PayrollDetailView.as_view(), name='payroll_details'),
    path('payroll/create/',  PayrollCreateView.as_view(), name=' payroll_create'),
    path('payroll/<int:pk>/',  PayrollUpdateView.as_view(), name='payroll_update'),
    path('payroll/<int:pk>/delete/',
         PayrollDeleteView.as_view(), name='payroll_delete'),


]
