from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'help_the_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^homeful/', include('homeful.urls', namespace="homeful")),
    url(r'^$', include('homeful.urls', namespace="homeful")),

)
