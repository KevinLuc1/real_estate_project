from django.db import models
from datetime import datetime
from realtors.models import Realtor

# models are created through a class
class Listing(models.Model):
    # use foreignkey to connect the Realtor model, we do not want to delete the listing if realtor is deleted
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    description = models.TextField(blank=True) #optional to fill in
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathroom = models.DecimalField(max_digits=3, decimal_places=1) #in case 1.5 or 2.5
    garage = models.IntegerField(default=0)
    squarefoot = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    #anything uploaded to imagefield in the admin area will go to the media folder
    #upload_to defines what folder we want to upload to inside that media folder
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DataTimeField(default=datetime.now, blank=True) #import datetime

    #using title to be the main field to be displayed
    def __str__(self):
        return self.title
    
