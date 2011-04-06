'''
Created on Apr 5, 2011

@author: Mike_Edwards
'''
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list import ListView
from EmoCaptcha.trainer.models import Term, AFINN111Score, Request
from django.views.generic.detail import DetailView
from EmoCaptcha.trainer.views import HomeView, SubmissionView
from piston.resource import Resource
from EmoCaptcha.trainer.handlers import RequestHandler, ResponseHandler

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='trainer_home'),
    
    url(r'^submit/$', SubmissionView.as_view(), name='trainer_submission'),

    url(r'^terms/$', ListView.as_view(model=Term), name="trainer_terms_list"),
    url(r'^terms/(?P<pk>\d+)/$', DetailView.as_view(model=Term), name="trainer_terms_detail"),
    url(r'^terms/a111/$', ListView.as_view(model=AFINN111Score), name="trainer_affin111_scores_list"),
    url(r'^terms/a111/(?P<pk>\d+)/$', DetailView.as_view(model=AFINN111Score), name="trainer_affin111_scores_detail"),

    url(r'^requests/$', ListView.as_view(model=Request), name="trainer_requests_list"),
    url(r'^requests/(?P<slug>\w+)/$', DetailView.as_view(model=Request), name="trainer_requests_detail"),
)

request_handler = Resource(RequestHandler)
response_handler = Resource(ResponseHandler)

urlpatterns += patterns('',
    url(r'^api/submit/$', SubmissionView.as_view(), {'to_api':True}, name='trainer_api_submission'),

    url(r'^api/requests/new/$', request_handler, name="trainer_requests_detail_api"),
    url(r'^api/requests/(?P<slug>\w+)/$', request_handler, name="trainer_requests_detail_api"),
    url(r'^api/responses/new/$', response_handler, name="trainer_responses_detail_api"),
)