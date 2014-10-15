from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from models import Poll, Answer


def show_poll(request, poll_name):
    poll = get_object_or_404(Poll, pk=poll_name)
    possible_dates = poll.possible_dates.order_by('date').all()
    answers = []
    for answer in poll.answers.prefetch_related('yes').prefetch_related('maybe').all():
        votes = []
        for date in possible_dates:
            if date in answer.yes.all():
                votes.append('yes')
            elif date in answer.maybe.all():
                votes.append('maybe')
            else:
                votes.append('no')
        answers.append({'name': answer.name, 'votes': votes})
    counts = [0.0 for _ in possible_dates]
    for answer in answers:
        for i, vote in enumerate(answer['votes']):
            if vote == 'yes':
                counts[i] += 1
            elif vote == 'maybe':
                counts[i] += 0.5
    return render(
        request,
        'datefinder/show.html',
        {
            'poll': poll,
            'answers': answers,
            'possible_dates': possible_dates,
            'counts': counts,
            'maxcount': max(counts)
        }
    )


def save_answer(request):
    print (request.POST)
    if not 'poll_name' in request.POST or not 'name' in request.POST:
        raise Http404
    poll_name = request.POST['poll_name']
    poll = get_object_or_404(Poll, pk=poll_name)
    answer = Answer(name=request.POST['name'], poll=poll)
    answer.save()  # We have to save the new answer to create a valid primary key
    for i, choice in enumerate(poll.possible_dates.all()):
        if 'choice' + str(i) in request.POST:
            if request.POST['choice' + str(i)] == 'yes':
                answer.yes.add(choice)
            elif request.POST['choice' + str(i)] == 'maybe':
                answer.maybe.add(choice)
    answer.save()
    return redirect('show_poll', poll_name=poll_name)