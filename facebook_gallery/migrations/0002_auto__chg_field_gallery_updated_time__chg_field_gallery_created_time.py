# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Gallery.updated_time'
        db.alter_column('facebook_gallery_gallery', 'updated_time', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Gallery.created_time'
        db.alter_column('facebook_gallery_gallery', 'created_time', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Gallery.updated_time'
        db.alter_column('facebook_gallery_gallery', 'updated_time', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Gallery.created_time'
        db.alter_column('facebook_gallery_gallery', 'created_time', self.gf('django.db.models.fields.DateField')())

    models = {
        'facebook_gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'album_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'cover_photo': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'facebook_gallery.image': {
            'Meta': {'object_name': 'Image'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facebook_gallery.Gallery']"}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['facebook_gallery']