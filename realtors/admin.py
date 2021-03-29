from django.contrib import admin

# Register your models here.

#sends this into the django admin
from .models import Realtor

#We can add certain variables here or properties that relate to how things are displayed
# we can customize our django admin with methods here without to instead of  having to go into the django admin code
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date') #choose items to display in admin page
    list_display_links = ('id', 'name') #choose which links are clickable to open file
    search_fields = ('name', ) #adds a box to search based off 'name'
    list_per_page = 20

admin.site.register(Realtor, RealtorAdmin)