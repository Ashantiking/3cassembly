from django.urls import path
from membership import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
