from django.contrib import admin
from .models import Payroll, Category, Status, Charity, Maintenance, Payment, Procurement
# Register your models here.


admin.site.register(Payroll)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Charity)
admin.site.register(Maintenance)
admin.site.register(Payment)
admin.site.register(Procurement)
