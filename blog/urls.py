from django.urls import path
from .views import PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('post/', PostView.as_view(), name='blog'),
    path('post/<pk>/<slug:slug>', PostDetailView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),


]
