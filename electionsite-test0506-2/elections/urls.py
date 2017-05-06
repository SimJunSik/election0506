from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index2.+/$', views.index2),
	url(r'^index3/$', views.index3),
	url(r'^index4/$', views.index4),
	#url(r'^polls/(?P<poll_id>\d+)/$',views.polls)
	#url(r'^polls/$',views.polls)
	url(r'^polls/(?P<poll_id>\d+)/$',views.polls)
]