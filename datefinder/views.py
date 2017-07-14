#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from datefinder.models import Poll, Answer


def show_poll(request, poll_name):
    poll = get_object_or_404(Poll, pk=poll_name)
    possible_dates = poll.possible_dates.order_by('date').all()
    answers = []
    counts = [0.0 for _ in possible_dates]
    for answer in poll.answers.prefetch_related('yes').prefetch_related('maybe').all():
        votes = []
        for i, date in enumerate(possible_dates):
            if date in answer.yes.all():
                votes.append('yes')
                counts[i] += 1
            elif date in answer.maybe.all():
                votes.append('maybe')
                counts[i] += 0.5
            else:
                votes.append('no')
        answers.append({'name': answer.name, 'votes': votes})
    rowspan_counts = {
        'years': {},
        'yearmonths': {},
        'yearmonthdays': {}
    }
    for date in possible_dates:
        if str(date.date.year) in rowspan_counts['years']:
            rowspan_counts['years'][str(date.date.year)] += 1
        else:
            rowspan_counts['years'][str(date.date.year)] = 1
        if str(date.date.year) + ':' + str(date.date.month) in rowspan_counts['yearmonths']:
            rowspan_counts['yearmonths'][str(date.date.year) + ':' + str(date.date.month)] += 1
        else:
            rowspan_counts['yearmonths'][str(date.date.year) + ':' + str(date.date.month)] = 1
        if str(date.date.year) + ':' + str(date.date.month) + ':' + str(date.date.day) in rowspan_counts['yearmonthdays']:
            rowspan_counts['yearmonthdays'][str(date.date.year) + ':' + str(date.date.month) + ':' + str(date.date.day)] += 1
        else:
            rowspan_counts['yearmonthdays'][str(date.date.year) + ':' + str(date.date.month) + ':' + str(date.date.day)] = 1
    dates = []
    for date in possible_dates:
        dates.append((
            date,
            rowspan_counts['years'][str(date.date.year)],
            rowspan_counts['yearmonths'][str(date.date.year) + ':' + str(date.date.month)],
            rowspan_counts['yearmonthdays'][str(date.date.year) + ':' + str(date.date.month) + ':' + str(date.date.day)]
        ))
    return render(
        request,
        'datefinder/show.html',
        {
            'poll': poll,
            'answers': answers,
            'possible_dates': dates,
            'counts': counts,
            'maxcount': max(counts)
        }
    )


def save_answer(request):
    if not 'poll_name' in request.POST or not 'name' in request.POST:
        raise Http404
    poll_name = request.POST['poll_name']
    poll = get_object_or_404(Poll, pk=poll_name)
    answer = Answer(name=request.POST['name'], poll=poll)
    answer.save()  # We have to save the new answer to create a valid primary key
    for i, choice in enumerate(poll.possible_dates.order_by('date').all()):
        if 'choice' + str(i) in request.POST:
            if request.POST['choice' + str(i)] == 'yes':
                answer.yes.add(choice)
            elif request.POST['choice' + str(i)] == 'maybe':
                answer.maybe.add(choice)
    answer.save()
    return redirect('show_poll', poll_name=poll_name)
