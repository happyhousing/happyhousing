from django.conf.urls import patterns, url

from homeful import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
)
