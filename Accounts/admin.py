from django.contrib import admin

from Accounts.models import User, UserProfile
from django.contrib.auth.admin import UserAdmin



class UserAdmin(UserAdmin): 
    list_display = ('email', 'first_name', 'last_name', 'created_date', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    list_display_links = ('email', 'username')
    filter_horizontal = () #filter_horizontal, list_filter and fieldsets would make the password fileds non editable
    list_filter = ()
    fieldsets = ()
    

class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state')
    list_display_links = ('user',)
    ordering = ('-created_at',)



admin.site.register(User, UserAdmin)

admin.site.register(UserProfile, UserprofileAdmin)