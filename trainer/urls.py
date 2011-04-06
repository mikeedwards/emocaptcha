'''
Created on Apr 5, 2011

@author: Mike_Edwards
'''
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list import ListView
from EmoCaptcha.trainer.models import Term, AFINN111Score
from django.views.generic.detail import DetailView
from EmoCaptcha.trainer.views import HomeView, SubmissionView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='trainer_home'),
    url(r'^submit/$', SubmissionView.as_view(), name='trainer_submission'),
    url(r'^terms/$', ListView.as_view(model=Term), name="trainer_terms_list"),
    url(r'^terms/(?P<pk>\d+)/$', DetailView.as_view(model=Term), name="trainer_terms_detail"),
    url(r'^terms/a111/$', ListView.as_view(model=AFINN111Score), name="trainer_affin111_scores_list"),
    url(r'^terms/a111/(?P<pk>\d+)/$', DetailView.as_view(model=AFINN111Score), name="trainer_affin111_scores_detail"),
)