#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from django.urls import include, path
from django.contrib import admin

urlpatterns = [ 
    path('dudel/', include('datefinder.urls')),
    path('admin/', admin.site.urls),
]
