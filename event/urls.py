from django.urls import path
from django.views.generic.edit import UpdateView
# , AddCategoryView, CategoryView
from .views import EventView, EventDetailView,  AddEventView, UpdateEventView, DeleteEventView

urlpatterns = [
    path('', EventView.as_view(), name='event'),
    path('detail/<int:pk>', EventDetailView.as_view(), name='event_details'),
    path('add_event/', AddEventView.as_view(), name='add_event'),
    path('event/edit/<int:pk>', UpdateEventView.as_view(), name='update_event'),
    path('event/<int:pk>/remove',
         DeleteEventView.as_view(), name='delete_event'),
]
