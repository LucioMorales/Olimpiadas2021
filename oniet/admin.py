from django.contrib import admin
from .models import *

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Info', {
          'fields': ('name','manager',)  
        }),
        ('Customer', {
            'fields': ('currentAmount','maxCapacity',)
        }),
    )
    list_display = ['id','name','manager','currentAmount','maxCapacity',]
    list_display_links = ['name','manager','currentAmount','maxCapacity',]

admin.site.register(Store,StoreAdmin)