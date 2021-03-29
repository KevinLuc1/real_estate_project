from django.contrib import admin

# Register your models here.

#sends this into the django admin
from .models import Realtor

admin.site.register(Realtor)