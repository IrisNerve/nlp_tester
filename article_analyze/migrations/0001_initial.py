# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'article_analyze_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'article_analyze', ['Article'])

        # Adding model 'Tag'
        db.create_table(u'article_analyze_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['article_analyze.Article'])),
            ('tag', self.gf('django.db.models.fields.TextField')()),
            ('service', self.gf('django.db.models.fields.IntegerField')()),
            ('vote', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'article_analyze', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'article_analyze_article')

        # Deleting model 'Tag'
        db.delete_table(u'article_analyze_tag')


    models = {
        u'article_analyze.article': {
            'Meta': {'object_name': 'Article'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'article_analyze.tag': {
            'Meta': {'object_name': 'Tag'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article_analyze.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.IntegerField', [], {}),
            'tag': ('django.db.models.fields.TextField', [], {}),
            'vote': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['article_analyze']