from django.urls import path
from django.views.generic.edit import UpdateView
# , AddCategoryView, CategoryView
from .views import HomeView, FaithView, FaithDetailView,  FaithCreateView, FaithUpdateView, FaithDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('faith/', FaithView.as_view(), name='faith'),
    path('detail/<int:pk>', FaithDetailView.as_view(), name='faith_details'),
    path('add_sfaith/', FaithCreateView.as_view(), name='add_faith'),
    path('faith/edit/<int:pk>', FaithUpdateView.as_view(), name='update_faith'),
    path('faith/<int:pk>/remove',
         FaithDeleteView.as_view(), name='delete_faith'),
]
