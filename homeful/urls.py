from django.conf.urls import patterns, url

from homeful import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^help/$', views.help, name='help'),
)
