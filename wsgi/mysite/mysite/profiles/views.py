from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DetailView, ListView

from django.contrib import messages

from account.mixins import LoginRequiredMixin

from .forms import ProfileForm
from .models import Profile

from django.db import models
#import star_rating 
from star_rating.models import Star_rating
from django.contrib.gis.geoip.base import GeoIP

from food.models import Grub

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
        #ctx['star_rating'] = Star_rating.objects.all()
        ctx['star_rating'] = Star_rating.objects.filter(profileName=ctx['profile'].user)
        ctx['grubbers'] = Grub.objects.all()
        return ctx


class ProfileListView(ListView):

    model = Profile
    context_object_name = "profiles"

    def get_context_data(self, **kwargs):
        ctx = super(ProfileListView, self).get_context_data(**kwargs)
        ctx['star_rating'] = Star_rating.objects.all()

        i=-1;
        for profile in ctx['profiles']:
            i = i+1
            j=0
            for star_rating in ctx['star_rating']:
                
                #print "blah=" + str(profile.user)
                if str(profile.user) == star_rating.profileName:
                    j=j+1
                    
                    try:
                        ctx['profiles'][i].totalAmount = ctx['profiles'][i].totalAmount + star_rating.rating
                        ctx['profiles'][i].starsCount = ctx['profiles'][i].starsCount +1
                        #ctx['profiles'][i]['stars'] =1
                        ctx['profiles'][i].stars =  float(ctx['profiles'][i].totalAmount/ctx['profiles'][i].starsCount)
                        print ctx['profiles'][i].stars                                                
                    except:
                        print('except')
                        setattr(ctx['profiles'][i], 'stars', int(star_rating.rating))
                        setattr(ctx['profiles'][i], 'totalAmount', int(star_rating.rating))
                        setattr(ctx['profiles'][i], 'starsCount', 1)

                    #ctx['profiles'][i]['stars'] = 6


        
        ctx['ip'] = self.request.META.get('REMOTE_ADDR', None)
        g = GeoIP()
        ip =  self.request.META.get('REMOTE_ADDR', None)
        if ip == '127.0.0.1':
            city='Seoul'
        if ip:
            city = g.city(ip)
            if ip == '127.0.0.1':
                city=city
            elif city == None:
                city= 'Seoul, KR'
            else:
                city = city['city']
                
            if city == None:
                city= 'Seoul, KR'



        else:
            city = 'New York' # default city

        ctx['city'] = city
        return ctx
