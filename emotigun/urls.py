'''
Created on Apr 5, 2011

@author: Mike_Edwards
'''
from django.conf.urls.defaults import patterns, url
from EmoCaptcha.emotigun.views import GameView

urlpatterns = patterns('',
    url(r'^$', GameView.as_view(), name='emotigun_game'),
)