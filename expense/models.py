from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('status')


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category')


class Payroll(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='payroll/%y', blank=True, null=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    id_number = models.CharField(max_length=4)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=4, blank=True, null=True)
    payroll_salary = models.IntegerField(blank=True, null=True)
    payroll_allowance = models.IntegerField(blank=True, null=True)
    payroll_accomodation = models.IntegerField(blank=True, null=True)
    date_employed = models.DateField()
    nok_address = models.CharField(max_length=255)
    nok_contact = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.ManyToManyField(Status, related_name='payroll_status')
    sum = models.IntegerField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name + ":  " + str(self.contact)

    # def save(self, *args, **kwargs):
    #    self.sum = self.payroll_salary + self.payroll_allowance + \
    #        self.payroll_accomodation
    #    super(Payroll, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('payroll')


class Charity(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='charity', blank=True, null=True)
    amount = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True)
    description = models.TextField()
    category = models.ManyToManyField(
        Category, related_name='charity_category')
    status = models.ManyToManyField(Status, related_name='charity_status')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name + ": " + str(self.amount)

    def get_absolute_url(self):
        return reverse('charity')


class Maintenance(models.Model):
    amount = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True)
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(
        Category, related_name='maintenance_category')
    status = models.ManyToManyField(Status, related_name='maintenance_status')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name + ": " + str(self.amount)

    def get_absolute_url(self):
        return reverse('maintenance')
