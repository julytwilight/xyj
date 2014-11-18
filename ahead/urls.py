from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ahead.views.home', name='home'),
    url(r'^', include('guys.urls')),
    url(r'^', include('shops.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Django Rest Framework
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)