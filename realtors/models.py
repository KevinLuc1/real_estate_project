from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=250)
    #anything uploaded to imagefield in the admin area will go to the media folder
    #upload_to defines what folder we want to upload to inside that media folder
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True) #optional to fill in
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=75)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    #using realtor name to be the main field to be displayed
    def __str__(self):
        return self.name