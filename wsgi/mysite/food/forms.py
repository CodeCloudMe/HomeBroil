import re

from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

from .models import Grub


class GrubForm(forms.ModelForm):

    class Meta:
        model = Grub
        fields = [
            "title",
            "photo",
            "description",
            "exp_date",
            "pub_date",
            "feeds",
            "price",
            "location",
        ]
    
    """
    def create_grub(sender, **kw):
        print "hi"
        grubIns = kw["instance"]
        if kw["created"]:
            grub = Grub(user=grubIns)
            grub.save()


    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        self.exp_date = timezone.now()
        self.userId = 5
        #print "hello"
        #super(Grub, self).save(*args, **kwargs)


"""

"""
def create_grub(sender, **kw):
        print "hi"
        grubIns = kw["instance"]
        if kw["created"]:
            grub = Grub(grub=grubIns)
            grub.save()   

"""     

"""
def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        self.exp_date = timezone.now()
        self.userId = 5
        #print "hello"
        super(Grub, self).save(*args, **kwargs)
"""

#post_save.connect(save, sender=Grub)

