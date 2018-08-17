"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include
from django.conf.urls import *
from tastypie.api import *
#from fabric.api import *
from secondproject.api.seconduser import FirstpageResource, SecondpageResource
from secondproject.Views import main

v2_api = Api(api_name='v2')
v2_api.register(FirstpageResource())
v2_api.register(SecondpageResource())

urlpatterns = patterns('',

                       (r'', include(v2_api.urls)),
                       url(r'^regist/$', main.register22),
                       (r'', include((v2_api.urls))),
                       url(r'^ord/$', main.order24),

                       )
