#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from django.conf.urls import url
from datefinder.views import save_answer, show_poll

urlpatterns = [
    url(r'^save_answer$', save_answer, name='save_answer'),
    url(r'^(?P<poll_name>(.*))$', show_poll, name='show_poll'),
]
