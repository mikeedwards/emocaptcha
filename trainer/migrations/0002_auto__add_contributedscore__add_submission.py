# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContributedScore'
        db.create_table('trainer_contributedscore', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contributed_scores', to=orm['trainer.Term'])),
            ('valence', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('arousal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dominance', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('trainer', ['ContributedScore'])

        # Adding model 'Submission'
        db.create_table('trainer_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(related_name='submissions', to=orm['trainer.Term'])),
            ('valence', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('arousal', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('dominance', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('trainer', ['Submission'])


    def backwards(self, orm):
        
        # Deleting model 'ContributedScore'
        db.delete_table('trainer_contributedscore')

        # Deleting model 'Submission'
        db.delete_table('trainer_submission')


    models = {
        'trainer.afinn111score': {
            'Meta': {'object_name': 'AFINN111Score'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'afinn111_scores'", 'to': "orm['trainer.Term']"}),
            'valence': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'trainer.contributedscore': {
            'Meta': {'object_name': 'ContributedScore'},
            'arousal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dominance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contributed_scores'", 'to': "orm['trainer.Term']"}),
            'valence': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'trainer.submission': {
            'Meta': {'object_name': 'Submission'},
            'arousal': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dominance': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submissions'", 'to': "orm['trainer.Term']"}),
            'valence': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'trainer.term': {
            'Meta': {'object_name': 'Term'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['trainer']
