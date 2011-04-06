# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'ContributedScore.arousal'
        db.delete_column('trainer_contributedscore', 'arousal')

        # Deleting field 'ContributedScore.dominance'
        db.delete_column('trainer_contributedscore', 'dominance')

        # Deleting field 'Submission.arousal'
        db.delete_column('trainer_submission', 'arousal')

        # Deleting field 'Submission.dominance'
        db.delete_column('trainer_submission', 'dominance')

        # Changing field 'Submission.valence'
        db.alter_column('trainer_submission', 'valence', self.gf('django.db.models.fields.FloatField')())


    def backwards(self, orm):
        
        # Adding field 'ContributedScore.arousal'
        db.add_column('trainer_contributedscore', 'arousal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'ContributedScore.dominance'
        db.add_column('trainer_contributedscore', 'dominance', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'Submission.arousal'
        db.add_column('trainer_submission', 'arousal', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'Submission.dominance'
        db.add_column('trainer_submission', 'dominance', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True), keep_default=False)

        # Changing field 'Submission.valence'
        db.alter_column('trainer_submission', 'valence', self.gf('django.db.models.fields.SmallIntegerField')(null=True))


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
        'trainer.submission': {
            'Meta': {'object_name': 'Submission'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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
