from django.conf.urls import patterns, include, url
from main import views
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aalto_fitness.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^favicon\.ico$', RedirectView.as_view(url='static/images/ico/favicon.ico')),
    # (r'^sitemap\.xml$', RedirectView.as_view(url='static/sitemap.xml')),

    url(r'^$', views.home_view),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)