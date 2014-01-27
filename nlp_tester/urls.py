from django.conf.urls import patterns, include, url

from nlp_tester.settings import STATIC_ROOT

urlpatterns = patterns('',
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': STATIC_ROOT, 'show_indexes': True}),
)

urlpatterns += patterns('nlp_tester.views',
    (r'^$', 'index'),
    (r'^analyze/$', 'analyze_url'),
)
