from django.db import models
from django.utils.timezone import now
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category')


class Income(models.Model):
    amount = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='category')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.category + ": " + str(self.amount)

    def get_absolute_url(self):
        return reverse('income')
