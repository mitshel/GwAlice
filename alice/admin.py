from django.contrib import admin
from .models import Log

# Register your models here.
# admin.site.register(Log)
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['request', 'response', 'created']
    list_filter = ['request', 'response', 'created']
    search_fields = ['request', 'response']
    date_hierarchy = 'created'