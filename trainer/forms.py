'''
Created on Apr 5, 2011

@author: Mike_Edwards
'''
from django.forms.models import ModelForm, ModelChoiceField
from EmoCaptcha.trainer.models import Submission, Term
from django.forms.formsets import formset_factory
from django.forms.fields import CharField, FloatField
from django.forms.widgets import HiddenInput, TextInput

class SubmissionForm(ModelForm):    
    term = ModelChoiceField(Term.objects.all(),widget=HiddenInput) 
    valence = FloatField(initial="0",widget=HiddenInput(attrs={"class":"valence-input"})) 
    class Meta:
        exclude = ['ip',]
        model = Submission
        
SubmissionFormset = formset_factory(SubmissionForm,extra=0)
