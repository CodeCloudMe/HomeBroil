import re

from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
        ]

    def create_grub(sender, **kw):
        print "hi"
        grubIns = kw["instance"]
        if kw["created"]:
            grub = Grub(grub=grubIns)
            grub.save()

    post_save.connect(create_grub, sender=Grub)
