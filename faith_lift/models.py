from django.db import models
from category.models import Category
# Create your models here.


class Faith(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='faith_lift', blank=True, null=True)
    video = models.FileField(upload_to='faith_lift/%y', blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='faith_category')
    date_added = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.name + ": " + str(self.video)

    def get_absolute_url(self):
        return reverse('faith')
