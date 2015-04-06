from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'main.views.index'),
    url(r'^register/', 'main.views.register'),
    url(r'^login/', 'main.views.login'),
    url(r'^logout/', 'main.views.logout'),

    url(r'^forum/', 'main.views.forum'),

    url(r'^admin/', include(admin.site.urls)),
)
