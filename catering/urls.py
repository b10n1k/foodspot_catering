from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from catering import views

urlpatterns = patterns("",
                       url(r'^home$', 'catering.views.home', name='home'),
                       url(r'^about$', 'catering.views.about', name='about'),
                       url(r'^contact$', 'catering.views.contact', name='contact'),
                       url(r'^services$', 'catering.views.services', name='services'),
                       url(r'^cataloge$', 'catering.views.cataloge', name='cataloge'),
                       url(r'^specials$', 'catering.views.specials', name='specials'),
                       
                       #url(r'^gallery$', include('imagestore.urls', namespace='imagestore')),
                       )
