from django.conf.urls import patterns, include, url

from nlp_tester.settings.base import STATIC_ROOT

urlpatterns = patterns('',
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': STATIC_ROOT, 'show_indexes': True}),
)

urlpatterns += patterns('article_analyze.views',
    (r'^$', 'index'),
    (r'^analyze/$', 'analyze_url'),
    (r'^upvote/$', 'tag_vote'),
)
