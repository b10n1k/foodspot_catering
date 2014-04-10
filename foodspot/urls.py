from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^foo/',include('catering.urls',namespace='catering')),
    #url(r'^contact/$','contact.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^photologue/', include('photologue.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG: 
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}) 
    ) 
