from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

from models import User

import os
import random, string
#from djangoratings.fields import RatingField
# Create your models here.

def food_upload(instance, filename):
    ext = filename.split(".")[-1]
    #filename = "%s.%s" % (uuid.uuid4(), ext)
    filename = ''.join(random.choice(string.lowercase) for i in range(10))
    filename =  "%s.%s" % (filename, ext)
    #return os.path.join("grub", filename) + ".png"
    return os.path.join("grub", filename)


class Grub(models.Model):
    title = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date added', blank=True)
    exp_date = models.DateTimeField('date expires', blank=True)
    description = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(upload_to=food_upload)
    #userId = models.IntegerField(blank=True)
    userId = models.ForeignKey(User)
    price = models.IntegerField(blank=True)
    feeds = models.IntegerField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    #rating = RatingField(range=5) # 5 possible rating values, 1-5



    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        self.exp_date = timezone.now()
        self.userId = User.objects.get()
        return super(Grub, self).save(*args, **kwargs)


        #print "hello"
       

    



    #


     


