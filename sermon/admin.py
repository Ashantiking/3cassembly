
from django.contrib import admin
from .models import Sermon, Category, Language, Status
# Register your models here.


class SermonAdmin(admin.ModelAdmin):
    list_display = ('theme', 'date_added')
    list_filter = ('category', 'language', 'status',
                   'views_count', 'date_added', 'updated_on')

    search_fields = ('theme',)
    # this create the slug field from the title field


admin.site.register(Sermon, SermonAdmin)

# TagAdmin must define "search_fields", because it's referenced by PostAdmin.autocomplete_fields.


class LanguageAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Language, LanguageAdmin)


class StatusAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Status, StatusAdmin)
