from django.urls import path
from django.views.generic.edit import UpdateView
# , AddCategoryView, CategoryView
from .views import SermonView, SermonDetailView,  SermonCreateView, SermonUpdateView, SermonDeleteView

urlpatterns = [
    path('', SermonView.as_view(), name='sermon'),
    path('detail/<int:pk>', SermonDetailView.as_view(), name='sermon_details'),
    path('add_sermon/', SermonCreateView.as_view(), name='add_sermon'),
    path('sermon/edit/<int:pk>', SermonUpdateView.as_view(), name='update_sermon'),
    path('sermon/<int:pk>/remove',
         SermonDeleteView.as_view(), name='delete_sermon'),
]
