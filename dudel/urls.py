#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [ 
    url(r'^dudel/', include('datefinder.urls')),
    url(r'^admin/', admin.site.urls),
]
