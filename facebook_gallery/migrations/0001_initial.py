# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('facebook_gallery_gallery', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cover_photo', self.gf('django.db.models.fields.URLField')(default='', max_length=200)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('album_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_time', self.gf('django.db.models.fields.DateField')()),
            ('updated_time', self.gf('django.db.models.fields.DateField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('facebook_gallery', ['Gallery'])

        # Adding model 'Image'
        db.create_table('facebook_gallery_image', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facebook_gallery.Gallery'])),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('facebook_gallery', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('facebook_gallery_gallery')

        # Deleting model 'Image'
        db.delete_table('facebook_gallery_image')


    models = {
        'facebook_gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'album_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'cover_photo': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'}),
            'created_time': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_time': ('django.db.models.fields.DateField', [], {})
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