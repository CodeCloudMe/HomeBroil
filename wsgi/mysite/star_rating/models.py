from django.db import models
import uuid
#from django.db.models.signals import post_save
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
from django.utils import timezone

import os
#import random, string
#from djangoratings.fields import RatingField
# Create your models here.


#profile is person being rated... user is person doing rating

class Star_rating(models.Model):
    profileId = models.IntegerField(blank=True)
    profileName = models.CharField(max_length=200, blank=True)
    grubId = models.IntegerField(blank=True)
    date_rated = models.DateTimeField('date rated', blank=True)
    userId = models.IntegerField(blank=True)
    userName = models.CharField(max_length=200, blank=True)
    rating = models.IntegerField(blank=True)
    
    #rating = RatingField(range=5) # 5 possible rating values, 1-5



    def save(self, *args, **kwargs):
        self.date_rated = timezone.now()
        #self.userId =  request.user.id
        #self.userName="hello"
        #self.grubId=2
        #self.profileName="mike"
        #self.rating=2
        #self.profileId=2

        return super(Star_rating, self).save(*args, **kwargs)


        #print "hello"
       

    



    #


     


