# Create your views here.
from django.views.generic.base import TemplateView
from EmoCaptcha.trainer.forms import SubmissionForm, SubmissionFormset
from EmoCaptcha import settings
from random import shuffle
from EmoCaptcha.trainer.models import Submission, Term
import math

class HomeView(TemplateView):
    template_name = "trainer/base.html"
    
class SubmissionView(TemplateView):
    template_name = "trainer/submission.html"

    def get_context_data(self, **kwargs):
        context = super(SubmissionView,self).get_context_data(**kwargs)
        shuffle(settings.WORDS)
        
        context['random_word'] = settings.WORDS[0]
        
        terms = list(Term.objects.all())
        shuffle(terms)
        
        random_terms = terms[:4]
        
        initial = []
        
        for term in random_terms:
            initial.append({'term':term})
        
        initial.append({'term':Term.objects.create(body = settings.WORDS[0])})
        
        shuffle(initial)

        formset = SubmissionFormset(initial=initial)

        context['formset'] = formset

        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        formset = SubmissionFormset(self.request.POST)
        
        humanity_delta = 0
        human_test = True

        for form in formset.forms:
            if form.is_valid():
                submission = form.save(False)
                submission.ip = self.request.META["REMOTE_ADDR"]
                submission.save()
                if len(submission.term.afinn111_scores.all()) > 0:
                    humanity_delta += abs(submission.term.afinn111_scores.all()[0].valence - submission.valence)

        if humanity_delta > 4:
            human_test = False

        self.template_name = "trainer/receipt.html"
        
        context['formset'] = formset
        context['humanity'] = {'delta':humanity_delta,'test':human_test}
        
        return self.render_to_response(context)