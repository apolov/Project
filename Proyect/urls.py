from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'login.views.welcome', name='welcome'),
    url(r'^auth/$', 'login.views.auth_view', name='auth_view'),
    url(r'^logout/$', 'login.views.logout', name='logout'),
    url(r'^loggedin/$', 'login.views.loggedin', name='loggedin'),
    url(r'^invalid/$', 'login.views.invalid_login', name='invalid_login'),
    # url(r'^Proyect/', include('Proyect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
