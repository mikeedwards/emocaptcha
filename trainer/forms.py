'''
Created on Apr 5, 2011

@author: Mike_Edwards
'''
from django.forms.models import ModelForm, ModelChoiceField
from EmoCaptcha.trainer.models import Submission, Term, Response, Request
from django.forms.formsets import formset_factory
from django.forms.fields import CharField, FloatField, SlugField
from django.forms.widgets import HiddenInput, TextInput

class SubmissionForm(ModelForm):    
    request = ModelChoiceField(Request.objects.all(),widget=HiddenInput,to_field_name="slug") 
    term = ModelChoiceField(Term.objects.all(),widget=HiddenInput,to_field_name="body") 
    valence = FloatField(initial="0",widget=HiddenInput(attrs={"class":"valence-input"})) 
    class Meta:
        model = Submission
        
SubmissionFormset = formset_factory(SubmissionForm,extra=0)

class ResponseForm(ModelForm):    
    term = ModelChoiceField(Term.objects.all(),widget=HiddenInput) 
    valence = FloatField(initial="0",widget=HiddenInput(attrs={"class":"valence-input"}))
    request = SlugField() 
    class Meta:
        model = Response
        
