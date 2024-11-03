from django.contrib import admin
from .models import vendor

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'VendorName', 'vendorType', 'IsApproved', 'CreatedAt')
    list_display_links = ('user', 'VendorName')
    list_editable = ('IsApproved',)

admin.site.register(vendor, VendorAdmin)