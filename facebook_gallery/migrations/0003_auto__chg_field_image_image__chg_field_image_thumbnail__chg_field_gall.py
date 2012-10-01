# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Image.image'
        db.alter_column('facebook_gallery_image', 'image', self.gf('django.db.models.fields.URLField')(max_length=255))

        # Changing field 'Image.thumbnail'
        db.alter_column('facebook_gallery_image', 'thumbnail', self.gf('django.db.models.fields.URLField')(max_length=255))

        # Changing field 'Gallery.cover_photo'
        db.alter_column('facebook_gallery_gallery', 'cover_photo', self.gf('django.db.models.fields.URLField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Image.image'
        db.alter_column('facebook_gallery_image', 'image', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'Image.thumbnail'
        db.alter_column('facebook_gallery_image', 'thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'Gallery.cover_photo'
        db.alter_column('facebook_gallery_gallery', 'cover_photo', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        'facebook_gallery.gallery': {
            'Meta': {'ordering': "['created_time', 'updated_time', 'name']", 'object_name': 'Gallery'},
            'album_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'cover_photo': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '255'}),
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
            'image': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['facebook_gallery']