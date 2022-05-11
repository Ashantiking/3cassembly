
from django.contrib import admin
from .models import Faith
# Register your models here.


class FaithAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    list_filter = ('category', 'video', 'date_added', 'updated_on')

    search_fields = ('name',)
    # this create the slug field from the title field


admin.site.register(Faith, FaithAdmin)

# TagAdmin must define "search_fields", because it's referenced by PostAdmin.autocomplete_fields.
