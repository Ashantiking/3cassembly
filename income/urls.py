
####################################################################
# INCOME SECTION URLS #
###################################################################

from django.urls import path
from .views import IncomeView, IncomeDetailView, IncomeCreateView, IncomeUpdateView, IncomeDeleteView


urlpatterns = [
    path('',  IncomeView.as_view(), name='income'),
    path('income/<int:pk>/',  IncomeDetailView.as_view(), name='income_details'),
    path('income/create/',  IncomeCreateView.as_view(), name=' income_create'),
    path('income/<int:pk>/',  IncomeUpdateView.as_view(), name='income_update'),
    path('income/<int:pk>/delete/',
         IncomeDeleteView.as_view(), name='income_delete'),


]
