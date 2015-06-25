from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

import os
import random, string

# Create your models here.

def food_upload(instance, filename):
    ext = filename.split(".")[-1]
    #filename = "%s.%s" % (uuid.uuid4(), ext)
    filename = ''.join(random.choice(string.lowercase) for i in range(10))
    return os.path.join("grub", filename)


class Grub(models.Model):
    title = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date added', blank=True)
    exp_date = models.DateTimeField('date expires', blank=True)
    description = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(upload_to=food_upload,  blank=True)
    userId = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    feeds = models.IntegerField(blank=True)
    location = models.CharField(max_length=200, blank=True)


    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        self.exp_date = timezone.now()
        self.userId = 5
        return super(Grub, self).save(*args, **kwargs)


        #print "hello"
       

    



    #


     


