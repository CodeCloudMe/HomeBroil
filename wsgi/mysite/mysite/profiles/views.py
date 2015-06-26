from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DetailView, ListView

from django.contrib import messages

from account.mixins import LoginRequiredMixin

from .forms import ProfileForm
from .models import Profile

from django.db import models
#import star_rating 
from star_rating.models import Star_rating

#import star_rating


class ProfileEditView(LoginRequiredMixin, UpdateView):

    form_class = ProfileForm
    model = Profile

    def get_object(self):
        return self.request.user.get_profile()

    def get_success_url(self):
        return reverse("profiles_list")

    def form_valid(self, form):
        response = super(ProfileEditView, self).form_valid(form)
        messages.success(self.request, "You successfully updated your profile.")
        return response


class ProfileDetailView(DetailView):

    model = Profile
    slug_url_kwarg = "username"
    slug_field = "user__username"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        ctx = super(ProfileDetailView, self).get_context_data(**kwargs)
        ctx['star_rating'] = Star_rating.objects.all()
        return ctx


class ProfileListView(ListView):

    model = Profile
    context_object_name = "profiles"
