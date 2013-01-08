from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
from jordanmessina.filehelpers import ROOT, path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#initialize empty urls. we need the catch all tag_id regex has to be the LAST thing in urls
urlpatterns = patterns('',)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(?P<path>favicon\.png)$', 'django.views.static.serve', {'document_root': path(ROOT, '../media/')}),
        (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': path(ROOT, '../media/img/')}),
        (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': path(ROOT, '../media/js/')}),
        (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': path(ROOT, '../media/css/')}),
    )

urlpatterns += patterns('',
    url(r'^$', 'jordanmessina.views.index'),
    url(r'^archives$', 'jordanmessina.views.archives'),
    url(r'^about$', direct_to_template, {'template': 'about.html'}),
    url(r'^(?P<path>.*)$', 'jordanmessina.views.load_post'),
)
