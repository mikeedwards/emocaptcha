# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Term'
        db.create_table('trainer_term', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('trainer', ['Term'])

        # Adding model 'AFINN111Score'
        db.create_table('trainer_afinn111score', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(related_name='afinn111_scores', to=orm['trainer.Term'])),
            ('valence', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('trainer', ['AFINN111Score'])


    def backwards(self, orm):
        
        # Deleting model 'Term'
        db.delete_table('trainer_term')

        # Deleting model 'AFINN111Score'
        db.delete_table('trainer_afinn111score')


    models = {
        'trainer.afinn111score': {
            'Meta': {'object_name': 'AFINN111Score'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'afinn111_scores'", 'to': "orm['trainer.Term']"}),
            'valence': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'trainer.term': {
            'Meta': {'object_name': 'Term'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['trainer']
