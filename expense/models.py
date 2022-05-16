from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'Status'

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
    salary = models.IntegerField(blank=True, null=True)
    allowance = models.IntegerField(blank=True, null=True)
    accomodation = models.IntegerField(blank=True, null=True)
    date_employed = models.DateField()
    bank_name = models.CharField(max_length=255)
    account_title = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    nok_name = models.CharField(max_length=255)
    nok_address = models.CharField(max_length=255)
    nok_contact = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.ManyToManyField(Status, related_name='payroll_status')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name + ":  " + str(self.contact)

    def get_total_amount(self):
        return self.salary + self.allowance + self.accomodation

    def get_final_amount(self):
        return self.get_total_amount * self.counts(name)

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
    status = models.ManyToManyField(Status, related_name='maintenance_status')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name + ": " + str(self.amount)

    def get_absolute_url(self):
        return reverse('maintenance')


class Payment(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    name = models.ForeignKey(Payroll, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2,)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.ManyToManyField(Status, related_name='payment_status')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name + ": " + str(self.month)

    def get_absolute_url(self):
        return reverse('payment')


class Procurement(models.Model):
    name = models.CharField(max_length=255)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name + ":  " + str(self.quantity)

    def get_total_amount(self):
        return self.quantity * self.unit_price

    def get_final_amount(self):
        return self.get_total_amount * self.counts(name)

    def get_absolute_url(self):
        return reverse('procurement')
