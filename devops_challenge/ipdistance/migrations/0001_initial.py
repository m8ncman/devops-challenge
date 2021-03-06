# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IPRecord'
        db.create_table(u'ipdistance_iprecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.GenericIPAddressField')(unique=True, max_length=39)),
            ('lng', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'ipdistance', ['IPRecord'])


    def backwards(self, orm):
        # Deleting model 'IPRecord'
        db.delete_table(u'ipdistance_iprecord')


    models = {
        u'ipdistance.iprecord': {
            'Meta': {'object_name': 'IPRecord'},
            'address': ('django.db.models.fields.GenericIPAddressField', [], {'unique': 'True', 'max_length': '39'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        }
    }

    complete_apps = ['ipdistance']