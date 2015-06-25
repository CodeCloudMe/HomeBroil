#from django.shortcuts import render

# Create your views here

from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DetailView, ListView

from django.contrib import messages

from account.mixins import LoginRequiredMixin

#from .forms import ProfileForm
from .forms import GrubForm
from .models import Grub


import json

from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from django.contrib.auth.models import User
from django.contrib import messages

from account.decorators import login_required
from account.mixins import LoginRequiredMixin



class GrubCreateView(LoginRequiredMixin, CreateView):

    form_class = GrubForm
    model = Grub

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class GrubListView(ListView):

    model = Grub
    context_object_name = "grubs"



class GrubEditView(LoginRequiredMixin, UpdateView):

    form_class = GrubForm
    model = Grub

    def get_object(self):
        return self.request.user.get_profile()

    def get_success_url(self):
        return reverse("grubs_list")

    def form_valid(self, form):
        response = super(ProfileEditView, self).form_valid(form)
        messages.success(self.request, "You successfully updated your grub.")
        return response