# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'IPRecord.datetime'
        db.add_column(u'ipdistance_iprecord', 'datetime',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 3, 21, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'IPRecord.datetime'
        db.delete_column(u'ipdistance_iprecord', 'datetime')


    models = {
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