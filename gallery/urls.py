from django.urls import path
from django.views.generic.edit import UpdateView
from .views import AddGalleryView, GalleryView, GalleryDetailView,  AddGalleryView, UpdateGalleryView, DeleteGalleryView

urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),
    path('detail/<int:pk>', GalleryDetailView.as_view(), name='gallery_details'),
    path('add_gallery/', AddGalleryView.as_view(), name='add_gallery'),
    path('gallery/edit/<int:pk>', UpdateGalleryView.as_view(), name='update_gallery'),
    path('gallery/<int:pk>/remove',
         DeleteGalleryView.as_view(), name='delete_gallery'),
]
