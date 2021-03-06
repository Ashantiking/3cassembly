from django.contrib import admin
from .models import (
    Employee, Employee_preferences, Employment_record,
	Employee_hiring_details, Employee_company_loan, Employee_sss,
	Employee_pagibig, Employee_philhealth, Employee_comloan_contrib, Employee_resume,
    Employee_uniform, Employee_canteen, Employee_medical, Employee_gatepass, Employee_vale,
    Employee_sss_loan, Employee_pagibig_loan, Employee_sssloan_contrib, Employee_pagibigloan_contrib, Employee_canteen_contrib, Employee_medical_contrib,
    Employee_valeloan_contrib, Employee_acceptance, Employee_return_to_work, Employee_gatepass_contrib, Employee_citizenship
)
# Register your models here.

admin.site.register(Employee)
admin.site.register(Employee_preferences)
admin.site.register(Employment_record)
admin.site.register(Employee_hiring_details)
admin.site.register(Employee_company_loan)
admin.site.register(Employee_sss_loan)
admin.site.register(Employee_pagibig_loan)
admin.site.register(Employee_sss)
admin.site.register(Employee_pagibig)
admin.site.register(Employee_philhealth)
admin.site.register(Employee_comloan_contrib)
admin.site.register(Employee_sssloan_contrib)
admin.site.register(Employee_pagibigloan_contrib)
admin.site.register(Employee_resume)
admin.site.register(Employee_uniform)
admin.site.register(Employee_canteen)
admin.site.register(Employee_medical)
admin.site.register(Employee_gatepass)
admin.site.register(Employee_vale)
admin.site.register(Employee_valeloan_contrib)
admin.site.register(Employee_acceptance)
admin.site.register(Employee_return_to_work)
admin.site.register(Employee_canteen_contrib)
admin.site.register(Employee_medical_contrib)
admin.site.register(Employee_gatepass_contrib)
admin.site.register(Employee_citizenship)
