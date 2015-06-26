import re

from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

from .models import Star_rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Star_rating
        fields = [
            "profileId",
            "profileName",
            "userId",
            "userName",
            "date_rated",
            "rating",
            
        ]
    