from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from guys.views.accounts import RegisterView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ahead.views.home', name='home'),

    url(r'^whatsup/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^seeyou/$', 'guys.views.accounts.logout', name='logout'),
    url(r'^welcome/$', RegisterView.as_view(), name='register'),

    url(r'^', include('shops.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)