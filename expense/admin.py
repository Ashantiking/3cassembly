from django.contrib import admin
from .models import Payroll, Category, Status, Charity, Maintenance
# Register your models here.


admin.site.register(Payroll)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Charity)
admin.site.register(Maintenance)
