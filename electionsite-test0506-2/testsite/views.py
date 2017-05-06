from django.views.generic.base import TemplateView
from elections.models import HitCount
from elections.models import IPAdr, IPAdr2, IPAdr3, IPAdr4


from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

def HomeView(request) :
	#template_name = 'hhhhome.html'

	try:
		hc = HitCount.objects.get(pk=1)
	except:
		hc = HitCount(count=0)
		hc.save()
		pass
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')


	adrs = IPAdr.objects.all()

	cnt=0
	for adr in adrs :
		if adr.adr != ip :
			cnt = cnt+1
		else :
			break

	if cnt == len(adrs) :
		IPAdr.objects.create(adr=ip)
		hc = HitCount.objects.filter(pk=1)
		hc.update(count=F('count')+1)
		hc = HitCount.objects.get(pk=1)	

	context = {'count':hc.count}
	return render(request, 'hhhhome.html', context)

def RobotsView(request) :
	return render(request, 'robots.txt')

def SitemapView(request) :
	return render(request, 'sitemap.xml')