"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from testsite.views import HomeView
from elections.views import index
#from bookmark.views import *
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robots.txt/', views.RobotsView),
    url(r'^sitemap.xml/', views.SitemapView),
    url(r'^$', views.HomeView, name='home'),
    url(r'^elections/', include('elections.urls', namespace='elections')),
    #url(r'^polls/$',views.polls)
]
