from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BitMarket.views.home', name='home'),
    # url(r'^BitMarket/', include('BitMarket.foo.urls')),
    
    url(r'^$', 'BitMarket.index.views.index',name='home'),
    url(r'^aboutus/', 'BitMarket.index.views.aboutus'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
