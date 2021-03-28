from django.urls import path

from . import views

# this page is website.com/listing/ pointed by the main urls.py
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),

]
