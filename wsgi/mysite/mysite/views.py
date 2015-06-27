from django.shortcuts import render
from django.db import models

#import GeoIP

from django.contrib.gis.geoip.base import GeoIP

#gi.country_name_by_addr('64.233.161.99')
#g =geoip()

def homepage(request):
    if request.user.is_authenticated():
    	#g = geoip.HAS_GEOIP
    	g = GeoIP()
    	ip = request.META.get('REMOTE_ADDR', None)
    	if ip == '127.0.0.1':
    		city='Seoul'
    	if ip:
    		city = g.city(ip)
    		if ip == '127.0.0.1':
    		    city='Seoul'
    		if city == None:
    			city= 'Seoul'



    	else:
    		city = 'New York' # default city

        request.city = city
        request.ip = ip

        return render(request, "dashboard.html")
    else:
    	#g = geoip.HAS_GEOIP
    	g = GeoIP()
    	ip = request.META.get('REMOTE_ADDR', None)
    	if ip == '127.0.0.1':
    		city='Seoul'
    	if ip:
    		city = g.city(ip)
    		if ip == '127.0.0.1':
    		    city='Seoul'
    		if city == None:
    			city= 'Seoul'



    	else:
    		city = 'New York' # default city

        request.city = city
        request.ip = ip
        return render(request, "homepage.html")
