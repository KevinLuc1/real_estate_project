from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, price_choices, state_choices

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

    queryset_list = Listing.objects.order_by('-list_date')

    # check keywords
    if 'keywords' in request.GET:
        # save keyword values into var called keywords
        keywords = request.GET['keywords']
        if keywords: # make sure not blank
            queryset_list = queryset_list.filter(description__icontains=keywords) # icontiains searches for partial 

    # check by city
    if 'city' in request.GET:
        # save city values into var called city
        # inside the GET we're looking for something with a name="city" inside search.html
        city = request.GET['city']
        if city: # make sure not blank
            queryset_list = queryset_list.filter(city__iexact=city) #iexact is not case sensitive

    # check by state
    if 'state' in request.GET:
        # save state values into var called state
        state = request.GET['state']
        if state: # make sure not blank
            queryset_list = queryset_list.filter(state__iexact=state_choices[state]) #iexact is not case sensitive
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) # up to a certain price


    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

