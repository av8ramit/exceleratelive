from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'mysite.views.index', name='index'),
	url(r'^login/', include('userauth.urls', namespace='login')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^howitworks/$', 'mysite.views.howitworks', name='howitworks'),
    url(r'^whyitworks/$', 'mysite.views.whyitworks', name='whyitworks'),
    url(r'^extest/$', 'mysite.views.extest', name='extest'),
    url(r'^formtest/$', 'mysite.views.formtest', name='formtest'),
    url(r'^reports/$', 'mysite.views.reports', name='reports'),
)
