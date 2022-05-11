
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from category.models import Category
# Create your models here


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', blank=True, null=True)
    title = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery')
