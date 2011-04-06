from django.db import models
import zlib
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.db.models.signals import pre_save, post_save
from django.dispatch.dispatcher import receiver
import datetime
from random import shuffle
from EmoCaptcha import settings

class Term(models.Model):
    body = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.body
    
    def scores(): #@NoSelf
        doc = """Dictionary of scores related to this model""" #@UnusedVariable
       
        def fget(self):
            _scores = {}
            afinn111_scores = self.afinn111_scores.all()
            submissions = self.submissions.all()
            
            if len(afinn111_scores) > 0:
                _scores['afinn111_scores'] = afinn111_scores
            if len(submissions) > 0:
                _scores['submissions'] = submissions
                
            return _scores
           
        return locals()
       
    scores = property(**scores())
    
    @permalink
    def get_absolute_url(self):
        return ('trainer_terms_detail', (),{'pk':self.pk})
    
class AFINN111Score(models.Model):
    term = models.ForeignKey(Term,related_name="afinn111_scores")
    valence = models.SmallIntegerField()
    
    class Meta:
        verbose_name = "AFINN.111 score"
        verbose_name_plural = "AFINN.111 scores"
    
    @permalink
    def get_absolute_url(self):
        return ('trainer_afinn111_scores_detail', (),{'pk':self.pk})

    def __unicode__(self):
        return self.body
    
    
class Request(models.Model):
    slug = models.SlugField()
    ip = models.IPAddressField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    terms = models.ManyToManyField(Term,related_name="requests")

    @permalink
    def get_absolute_url(self):
        return ('trainer_requests_detail', (),{'slug':self.slug})

    def __unicode__(self):
        return self.slug
    

@receiver(pre_save)
def request_pre_save(sender, **kwargs):
    if sender == Request:
        request = kwargs['instance']
        if request.slug == "":
            request.slug = "%x" % (0xffffffff/2 + zlib.crc32(request.ip + str(datetime.datetime.now())))
            
@receiver(post_save)
def request_post_save(sender, **kwargs):
    if sender == Request:
        request = kwargs['instance']
        #seed the request with terms if it's new
        if len(request.terms.all()) == 0:
            shuffle(settings.WORDS)
            
            terms = list(Term.objects.all())
            shuffle(terms)
            
            random_terms = terms[:4]
            
            for term in random_terms:
                request.terms.add(term)
            
            random_term, created = Term.objects.get_or_create(body = settings.WORDS[0])
            request.terms.add(random_term)


class Response(models.Model):
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    request = models.ForeignKey(Request,related_name="responses")

    def delta(): #@NoSelf
        doc = """The difference between all submissions and canonical scores""" #@UnusedVariable
       
        def fget(self):
            _delta = 0
            _submissions = 0.0
            
            for submission in self.request.submissions.all():
                if len(submission.term.afinn111_scores.all()) > 0:
                    canon = submission.term.afinn111_scores.all()[0]
                    _delta += abs(canon.valence - submission.valence)
                    _submissions += 1.0
            
            if _submissions > 0.0:
                return _delta/_submissions
            else:
                return 10.0
           
        return locals()
       
    delta = property(**delta())
    
    def human(): #@NoSelf
        doc = """Is the submitter sufficiently human?""" #@UnusedVariable
       
        def fget(self):
            return self.delta < 1.0 
           
        return locals()
       
    human = property(**human())

    def __unicode__(self):
        return self.slug

@receiver(pre_save)
def response_pre_save(sender, **kwargs):
    if sender == Response:
        response = kwargs['instance']
        if response.slug == "":
            response.slug = "%x" % (0xffffffff/2 + zlib.crc32(response.request.ip + str(datetime.datetime.now())))



    
class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    term = models.ForeignKey(Term,related_name="submissions")
    valence = models.FloatField()
    request = models.ForeignKey(Request,related_name="submissions")
    
    def delta(): #@NoSelf
        doc = """The difference between the submission and canonical scores""" #@UnusedVariable
       
        def fget(self):
            if len(self.term.afinn111_scores.all()) > 0:
                canon = self.term.afinn111_scores.all()[0]
                return abs(canon.valence - self.valence)
            return None
           
        return locals()
       
    delta = property(**delta())
    
class ContributedScore(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    term = models.ForeignKey(Term,related_name="contributed_scores")
    valence = models.FloatField(null=True,blank=True)

