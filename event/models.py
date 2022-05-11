
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from category.models import Category
from datetime import datetime, date

# Create your models here


class Event(models.Model):
    image = models.ImageField(upload_to='event', blank=True, null=True)
    theme = models.CharField(max_length=255)
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.theme

    def get_absolute_url(self):
        return reverse('events')
