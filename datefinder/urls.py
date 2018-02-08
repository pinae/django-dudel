#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from django.urls import path
from datefinder.views import save_answer, show_poll

urlpatterns = [
    path('save_answer', save_answer, name='save_answer'),
    path('<str:poll_name>', show_poll, name='show_poll'),
]
