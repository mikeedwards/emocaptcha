# Create your views here.
from django.views.generic.base import TemplateView
from EmoCaptcha.trainer.forms import SubmissionFormset
from random import shuffle
from EmoCaptcha.trainer.models import Request, Response

class HomeView(TemplateView):
    template_name = "trainer/base.html"
    
class SubmissionView(TemplateView):
    template_name = "trainer/submission.html"

    def get_context_data(self, **kwargs):
        context = super(SubmissionView,self).get_context_data(**kwargs)
        
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        request = Request.objects.create(ip=self.request.META["REMOTE_ADDR"])
        
        initial = []
        
        for term in request.terms.all():
            initial.append({'request':request,'term':term})
        
        shuffle(initial)

        formset = SubmissionFormset(initial=initial)

        context['formset'] = formset
        
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        formset = SubmissionFormset(self.request.POST)
        
        if formset.is_valid():

            response = None 
    
            for form in formset.forms:
                if form.is_valid():
                    submission = form.save(False)
                    
                    #does this request already have a response?
                    if response is None:
                        if len(submission.request.responses.all()) > 0:
                            response = submission.request.responses.all()[0]
                            break
                        else:
                            response = Response()
                    
                    #does this response link to the request?    
                    try:
                        response.request
                    except (Request.DoesNotExist):
                        response.request = submission.request
                        response.save()
                        
                    #do the terms in the form match the request?
                    try: 
                        response.request.terms.get(body=form.cleaned_data["term"].body)
                        submission.save()
                    except:
                        print "Term does not exist in request"
                        break

            context['humanity'] = {'delta':response.delta,'test':response.human}

        self.template_name = "trainer/receipt.html"
        
        context['formset'] = formset
        
        return self.render_to_response(context)