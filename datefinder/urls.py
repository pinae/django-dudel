from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^save_answer$', 'datefinder.views.save_answer', name='save_answer'),
    url(r'^(?P<poll_name>(.*))$', 'datefinder.views.show_poll', name='show_poll'),
)