from django.db import models
import zlib
from django.core.urlresolvers import reverse
from django.db.models import permalink

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
    
    class Meta():
        verbose_name = "AFINN.111 score"
        verbose_name_plural = "AFINN.111 scores"
    
    @permalink
    def get_absolute_url(self):
        return ('trainer_afinn111_scores_detail', (),{'pk':self.pk})
    
class Submission(models.Model):
    ip = models.IPAddressField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    term = models.ForeignKey(Term,related_name="submissions")
    valence = models.FloatField()
    
class ContributedScore(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    term = models.ForeignKey(Term,related_name="contributed_scores")
    valence = models.FloatField(null=True,blank=True)

