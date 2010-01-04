from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('djangocon',
    url(r'^$', 'subscribers.views.home', name='home'),
    url(r'^clear/$', 'subscribers.views.clear', name='clear'),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^legal/$', 'direct_to_template', {'template': 'legal_notices.html'}, name='legal_notices'),
)

# Static Media File Serving
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )