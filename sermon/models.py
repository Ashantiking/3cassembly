from django.db import models
from django.conf import settings
from category.models import Category

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language')


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('status')


class Sermon(models.Model):
    theme = models.CharField(max_length=200, db_index=True)
    preached_by = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    video = models.FileField(upload_to='movies/%')
    image = models.ImageField(upload_to='movies')
    category = models.ManyToManyField(Category, related_name='sermon_category')
    language = models.ManyToManyField(Language, related_name='language')
    status = models.ManyToManyField(Status, related_name='status', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.theme + ": " + str(self.video)

    def get_absolute_url(self):
        return reverse('sermon')
