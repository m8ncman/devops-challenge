# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Distance'
        db.create_table(u'ipdistance_distance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('miles', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('from_ip', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_distances', to=orm['ipdistance.IPRecord'])),
            ('to_ip', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_distances', to=orm['ipdistance.IPRecord'])),
        ))
        db.send_create_signal(u'ipdistance', ['Distance'])


    def backwards(self, orm):
        # Deleting model 'Distance'
        db.delete_table(u'ipdistance_distance')


    models = {
        u'ipdistance.distance': {
            'Meta': {'object_name': 'Distance'},
            'from_ip': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_distances'", 'to': u"orm['ipdistance.IPRecord']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miles': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'to_ip': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_distances'", 'to': u"orm['ipdistance.IPRecord']"})
        },
        u'ipdistance.iprecord': {
            'Meta': {'object_name': 'IPRecord'},
            'address': ('django.db.models.fields.GenericIPAddressField', [], {'unique': 'True', 'max_length': '39'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        }
    }

    complete_apps = ['ipdistance']