from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.TextField(default='')


class PossibleDate(models.Model):
    poll = models.ForeignKey(Poll, related_name='possible_dates')
    date = models.DateTimeField()


class Answer(models.Model):
    poll = models.ForeignKey(Poll, related_name='answers')
    name = models.CharField(max_length=30)
    yes = models.ManyToManyField(PossibleDate, related_name='positive_answers')
    maybe = models.ManyToManyField(PossibleDate, related_name='maybe_answers')