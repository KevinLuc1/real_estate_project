from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

def index(request):
    #Fetch our listings using our model and then we insert our template, loop through and output the listing that are in the DB
    listings = Listing.objects.all().filter(is_published=True)

    # search paginator from django docs
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    # we can either pass in a dictionary as a 2nd param in render
    # ie: {'name': 'Kevin:} and inside html we use {{ name }}
    #w we can instead create a variable as a dictionary and pass in the variable 'context'
    return render(request, 'listings/listings.html', context)

# listing_id param is passed in through the url.py path'<int:listing_id>' which is through the browser listing/8 etc
def listing(request, listing_id): 
    # show 404 page if listing id does not exist
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')

