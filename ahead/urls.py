from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ahead.views.home.default', name='home'),

    url(r'^whatsup/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^seeyou/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^welcome/$', 'ahead.views.home.register', name='register'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)