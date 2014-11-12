from django.conf.urls import patterns, url

from userauth import views

urlpatterns = patterns('', 
		url(r'^$', 'userauth.views.home', name='front'),
		url(r'^register/$', 'userauth.views.register', name='register'),
		url(r'^auth/$', 'userauth.views.login_user', name='auth'),
		url(r'^sendregister/$', 'userauth.views.send', name='send'),
		url(r'^formtest2/$', 'userauth.views.formtest2', name='formtest2'),
		url(r'^upload/$', 'userauth.views.upload_file', name='upload'),
		url(r'^download/$', 'userauth.views.download_file', name='download'),
    	url(r'^downloadtest/$', 'userauth.views.download_test', name='downloadtest'),
    	url(r'^simple_report/$', 'userauth.views.simple_report', name='simple_report'),
    	url(r'^advanced_report/$', 'userauth.views.advanced_report', name='advanced_report'),
		# url(r'^sendregister/postregister/$', 'userauth.views.postregister', name='send_post'),
		)

