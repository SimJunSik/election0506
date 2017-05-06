from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.db.models import F

from .models import Candidate
from .models import Commitment
from .models import Category
from .models import Choice
from .models import Poll
from .models import HitCount

import datetime
# Create your views here.

def index(request) :
	candidates = Candidate.objects.all()
	commitments = Commitment.objects.all()
	category = Category.objects.all()
	json_serializer = serializers.get_serializer("json")()
	cmts = json_serializer.serialize(Commitment.objects.all(), ensure_ascii=False)
	context = {'commitments':commitments, 'categories':category, 'cmts' : cmts}

	return render(request, 'elections/index.html', context)



def index2(request) :
	json_serializer = serializers.get_serializer("json")()
	candidates = Candidate.objects.all()
	cmts = json_serializer.serialize(Commitment.objects.all(), ensure_ascii=False)
	commitments = Commitment.objects.all()
	category = Category.objects.all()

	today = datetime.datetime.now()
	try:
		poll = Poll.objects.get(start_date__lte=today, 
			end_date__gte=today)
	except:
		poll = None
	context = {'commitments':commitments, 'categories':category, 'cmts':cmts, 'poll': poll}


	return render(request, 'elections/index2.html', context)

def polls(request, poll_id):
	#poll_id = 1
	json_serializer = serializers.get_serializer("json")()
	cs = json_serializer.serialize(Choice.objects.all(), ensure_ascii=False)
	poll = Poll.objects.get(pk=poll_id)
	try :
		selection = request.POST['choice']
	except : 
		return render(request, 'elections/index4.html')
	c = [0,0,0,0,0]
	ch = Choice.objects.all()
	context = {'cs':cs}
	tmp = 0;

	for i in range(0,5) :
		c[i] = 0

	for i in range(0,len(selection)) :
		c[i] = selection[i:i+1]


	try:
		for j in range(0,len(selection)) :
			choice = Choice.objects.get(poll_id = 1, candidate_id = c[j])
			choice.votes += 1
			choice.save()
	except:
		for k in range(0,len(selection)) :
			choice = Choice(poll_id = 1, candidate_id = c[k], votes=1)
			choice.save()

	return render(request, 'elections/index4.html', context)

def index3(request) :
	candidates = Candidate.objects.all()
	commitments = Commitment.objects.all()
	category = Category.objects.all()
	context = {'commitments':commitments, 'categories':category}

	return render(request, 'elections/index3.html', context)


def index4(request) :
	candidates = Candidate.objects.all()
	commitments = Commitment.objects.all()
	category = Category.objects.all()
	context = {'commitments':commitments, 'categories':category}

	return render(request, 'elections/index4.html', context)



def areas(request) :
	return render(request, 'elections/area.html')