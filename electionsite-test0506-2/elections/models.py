from django.db import models

# Create your models here.

class Candidate(models.Model) :
	name = models.CharField(max_length=10)
	introduction = models.TextField()
	area = models.CharField(max_length=15)
	party_number = models.IntegerField(default=0)

	def __str__(self) :
		return self.name

class Poll(models.Model) :
	#idx = models.IntegerField(primary_key=True, default=1)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	#area = models.CharField(max_length=15)

class Choice(models.Model) :
	poll = models.ForeignKey(Poll)
	candidate = models.ForeignKey(Candidate)
	votes = models.IntegerField(default=0)

	def __str__(self) :
		return self.candidate.name

class Category(models.Model) :
	category = models.CharField(max_length=20)
	ctname = models.CharField(max_length=20, default='df')
	idx = models.IntegerField(default=0)

	def __str__(self) :
		return self.category

class Commitment(models.Model) :
	candidate = models.ForeignKey(Candidate)
	party_number = models.IntegerField(default=0)
	commitment = models.CharField(max_length=200)
	category = models.CharField(max_length=20)
	index = models.IntegerField(default=0)
	detail_cmmt = models.CharField(max_length=500, default=' ')
	ref = models.CharField(max_length=200, default=' ')
	imgsrc = models.CharField(max_length=100, default='../../static/img/1.png')
	#category = models.ForeignKey(Category)

	def __str__(self) :
		return self.commitment

class HitCount(models.Model):
    count = models.IntegerField()

class IPAdr(models.Model):
	adr = models.CharField(max_length=100)

class IPAdr2(models.Model):
	adr = models.CharField(max_length=100)

class IPAdr3(models.Model):
	adr = models.CharField(max_length=100)

class IPAdr4(models.Model):
	adr = models.CharField(max_length=100)