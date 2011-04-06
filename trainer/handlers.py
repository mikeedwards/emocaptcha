'''
Created on Apr 6, 2011

@author: Mike_Edwards
'''
from piston.handler import BaseHandler
from EmoCaptcha.trainer.models import Request, Response
from piston.utils import validate, throttle
from EmoCaptcha.trainer.forms import SubmissionForm, SubmissionFormset

class RequestHandler(BaseHandler):
    allowed_methods = ('GET','PUT',)
    model = Request
    fields = ('slug',
              ('terms',
                ('body',)
              ),
              ('responses',
                ('slug','human','delta')
              ),)
    
    @throttle(5, 60)
    def read(self, request, slug=None): 
        try:
            req = Request.objects.get(slug=slug)
        except (Request.DoesNotExist):
            req = Request.objects.create(ip=request.META["REMOTE_ADDR"])
        return req

class ResponseHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = Response
    fields = ('slug','human','delta',('request',('slug',('terms',('body',)))),)

    @throttle(5, 60)
    @validate(SubmissionFormset)
    def create(self,request):
        #formset = request.form
        
        formset = SubmissionFormset(request.POST)
        
        if not formset.is_valid():
            return None
        
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

                
        return response
