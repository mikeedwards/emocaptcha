# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field terms on 'Request'
        db.create_table('trainer_request_terms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('request', models.ForeignKey(orm['trainer.request'], null=False)),
            ('term', models.ForeignKey(orm['trainer.term'], null=False))
        ))
        db.create_unique('trainer_request_terms', ['request_id', 'term_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field terms on 'Request'
        db.delete_table('trainer_request_terms')


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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'terms': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'requests'", 'symmetrical': 'False', 'to': "orm['trainer.Term']"})
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
