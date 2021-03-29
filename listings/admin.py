from django.contrib import admin

# Register your models here.

#sends this into the django admin
from .models import Listing

#We can add certain variables here or properties that relate to how things are displayed
# we can customize our django admin with methods here without to instead of  having to go into the django admin code
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') #choose items to display in admin
    list_display_links = ('id', 'title') # allows you to choose which categories are clickable
    list_filter = ('realtor', ) # create a filer for said category
    list_editable = ('is_published', ) #turn true false into clickbale check box
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') #add searchable field
    list_per_page = 20

admin.site.register(Listing, ListingAdmin)