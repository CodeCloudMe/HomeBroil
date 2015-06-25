#from django.shortcuts import render

# Create your views here

from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DetailView, ListView

from django.contrib import messages

from account.mixins import LoginRequiredMixin

#from .forms import ProfileForm
from .models import Grub

class GrubListView(ListView):

    model = Grub
    context_object_name = "grubs"