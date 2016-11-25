"""HelloWorld URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from HelloWorld.view import hello
from HelloWorld.testdb import *
from HelloWorld import search
from HelloWorld import search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^hello/$', hello),
    url('^testdb/$', testdb),
    url('^testdb2/$', testdb2),
    url('^testdb3/$', testdb3),
    url('^testdb4/$', testdb4),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),
]
