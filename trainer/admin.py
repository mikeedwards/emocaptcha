'''
Created on Apr 5, 2011

@author: Mike_Edwards
'''
from django.contrib import admin
from EmoCaptcha.trainer.models import Term, AFINN111Score, Submission, Request,\
    Response
from django.contrib.admin.options import ModelAdmin

class AFINN111ScoreAdmin(ModelAdmin):
    list_display = ['term','valence',]

admin.site.register(Term)
admin.site.register(AFINN111Score,AFINN111ScoreAdmin)
admin.site.register(Submission)
admin.site.register(Request)
admin.site.register(Response)