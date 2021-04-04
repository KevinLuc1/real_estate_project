from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from listings.models import Listing

from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # sort by 3 most recent list date

    # to pass listings into html, we need to set it up as a dictionary and pass in the dictionary on the return render
    context = {
        'listings':listings
    }
    return render(request, 'pages/index.html', context) # pass context in index.html under pages app to grab listings 

def about(request):
    # get realtors from database
    realtors = Realtor.objects.order_by('-hire_date')

    # get mvp of month
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    # pass data into dictionary called context, context gets passed in the return render
    context = {
        'realtors': realtors, 
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
