# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tag.vote'
        db.alter_column(u'article_analyze_tag', 'vote', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'Tag.vote'
        db.alter_column(u'article_analyze_tag', 'vote', self.gf('django.db.models.fields.BooleanField')())

    models = {
        u'article_analyze.article': {
            'Meta': {'object_name': 'Article'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'article_analyze.tag': {
            'Meta': {'object_name': 'Tag'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article_analyze.Article']"}),
            'confidence': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.IntegerField', [], {}),
            'tag': ('django.db.models.fields.TextField', [], {}),
            'vote': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['article_analyze']