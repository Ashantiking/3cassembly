from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category')


class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    content_1 = models.TextField(blank=True, null=True)
    content_2 = models.TextField(blank=True, null=True)
    content_3 = models.TextField(blank=True, null=True)
    content_4 = models.TextField(blank=True, null=True)
    content_5 = models.TextField(blank=True, null=True)
    content_6 = models.TextField(blank=True, null=True)
    content_7 = models.TextField(blank=True, null=True)
    content_8 = models.TextField(blank=True, null=True)
    content_9 = models.TextField(blank=True, null=True)
    content_10 = models.TextField(blank=True, null=True)
    content_11 = models.TextField(blank=True, null=True)
    content_12 = models.TextField(blank=True, null=True)
    content_13 = models.TextField(blank=True, null=True)
    content_14 = models.TextField(blank=True, null=True)
    content_15 = models.TextField(blank=True, null=True)
    content_16 = models.TextField(blank=True, null=True)
    content_17 = models.TextField(blank=True, null=True)
    content_18 = models.TextField(blank=True, null=True)
    content_19 = models.TextField(blank=True, null=True)
    content_20 = models.TextField(blank=True, null=True)
    content_21 = models.TextField(blank=True, null=True)
    content_22 = models.TextField(blank=True, null=True)
    content_23 = models.TextField(blank=True, null=True)
    content_24 = models.TextField(blank=True, null=True)
    content_25 = models.TextField(blank=True, null=True)
    content_26 = models.TextField(blank=True, null=True)
    content_27 = models.TextField(blank=True, null=True)
    content_28 = models.TextField(blank=True, null=True)
    content_29 = models.TextField(blank=True, null=True)
    content_30 = models.TextField(blank=True, null=True)
    content_31 = models.TextField(blank=True, null=True)
    content_32 = models.TextField(blank=True, null=True)
    content_33 = models.TextField(blank=True, null=True)
    content_34 = models.TextField(blank=True, null=True)
    content_35 = models.TextField(blank=True, null=True)
    content_36 = models.TextField(blank=True, null=True)
    content_37 = models.TextField(blank=True, null=True)
    content_38 = models.TextField(blank=True, null=True)
    content_39 = models.TextField(blank=True, null=True)
    content_40 = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='book_category')
    pdf = models.FileField(upload_to='pdf')
    recommended_books = models.BooleanField(default=False)
    spiritual_growth_books = models.BooleanField(default=False)
    relationship_books = models.BooleanField(default=False)
    empowerment_books = models.BooleanField(default=False)
    movitational_books = models.BooleanField(default=False)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books')
