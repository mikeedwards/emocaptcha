'''
Created on Apr 5, 2011

@author: Mike_Edwards
'''
from django.views.generic.base import TemplateView
class HomeView(TemplateView):
    template_name = "home.html"