from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import driver

# Register your models here.

class driverAdmin(admin.ModelAdmin):
    list_display = ('user', 'driver_plate_reg', 'vehilce_type', 'IsApproved', 'CreatedAt')
    list_display_links = ('user', 'driver_plate_reg')
    list_editable = ('IsApproved',)

admin.site.register(driver, driverAdmin)