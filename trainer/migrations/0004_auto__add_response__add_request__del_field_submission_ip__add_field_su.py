# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Response'
        db.create_table('trainer_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(related_name='responses', to=orm['trainer.Request'])),
        ))
        db.send_create_signal('trainer', ['Response'])

        # Adding model 'Request'
        db.create_table('trainer_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('trainer', ['Request'])

        # Deleting field 'Submission.ip'
        db.delete_column('trainer_submission', 'ip')

        # Adding field 'Submission.request'
        db.add_column('trainer_submission', 'request', self.gf('django.db.models.fields.related.ForeignKey')(default='127.0.0.1', related_name='submissions', to=orm['trainer.Request']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Response'
        db.delete_table('trainer_response')

        # Deleting model 'Request'
        db.delete_table('trainer_request')

        # Adding field 'Submission.ip'
        db.add_column('trainer_submission', 'ip', self.gf('django.db.models.fields.IPAddressField')(default='127.0.0.1', max_length=15), keep_default=False)

        # Deleting field 'Submission.request'
        db.delete_column('trainer_submission', 'request_id')


    models = {
        'trainer.afinn111score': {
            'Meta': {'object_name': 'AFINN111Score'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'afinn111_scores'", 'to': "orm['trainer.Term']"}),
            'valence': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'trainer.contributedscore': {
            'Meta': {'object_name': 'ContributedScore'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contributed_scores'", 'to': "orm['trainer.Term']"}),
            'valence': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'trainer.request': {
            'Meta': {'object_name': 'Request'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'trainer.response': {
            'Meta': {'object_name': 'Response'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'responses'", 'to': "orm['trainer.Request']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'trainer.submission': {
            'Meta': {'object_name': 'Submission'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submissions'", 'to': "orm['trainer.Request']"}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submissions'", 'to': "orm['trainer.Term']"}),
            'valence': ('django.db.models.fields.FloatField', [], {})
        },
        'trainer.term': {
            'Meta': {'object_name': 'Term'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['trainer']
