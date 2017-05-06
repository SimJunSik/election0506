from django.contrib import admin

from .models import Candidate, Poll, Commitment, Category, Choice, HitCount, IPAdr , IPAdr2, IPAdr3, IPAdr4
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Poll)
admin.site.register(Commitment)
admin.site.register(Category)
admin.site.register(Choice)
admin.site.register(HitCount)
admin.site.register(IPAdr)
admin.site.register(IPAdr2)
admin.site.register(IPAdr3)
admin.site.register(IPAdr4)