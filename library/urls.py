from django.urls import path
from django.views.generic.edit import UpdateView
from .views import BookCreateView, BookView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookView.as_view(), name='book'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book_details'),
    path('add_book/', BookCreateView.as_view(), name='add_book'),
    path('book/edit/<int:pk>', BookUpdateView.as_view(), name='update_book'),
    path('book/<int:pk>/remove',
         BookDeleteView.as_view(), name='delete_book'),
]
