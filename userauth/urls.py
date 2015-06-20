from django.conf.urls import patterns, url

from userauth import views

urlpatterns = patterns('', 
		url(r'^$', 'userauth.views.home', name='front'),
		url(r'^register/$', 'userauth.views.register', name='register'),
		url(r'^auth/$', 'userauth.views.login_user', name='auth'),
		url(r'^sendregister/$', 'userauth.views.send', name='send'),
		url(r'^recoverpasswordpage/$', 'userauth.views.recover_password_page', name='recoverpasswordpage'),
		url(r'^recoverpassword/$', 'userauth.views.recover_password', name='recoverpassword'),
		url(r'^formtest2/$', 'userauth.views.formtest2', name='formtest2'),
		url(r'^upload/$', 'userauth.views.upload_file', name='upload'),
		url(r'^download/$', 'userauth.views.download_file', name='download'),
		url(r'^update_test_mode/$', 'userauth.views.update_test_mode', name='update_test_mode'),
		url(r'^downloadtest/$', 'userauth.views.download_test', name='downloadtest'),
		url(r'^testportal/$', 'userauth.views.testportal', name='testportal'),
    	url(r'^bubblesheet/$', 'userauth.views.bubblesheet', name='bubblesheet'),
       	url(r'^bubblesheet_omit/$', 'userauth.views.bubblesheet_omit', name='bubblesheet_omit'),
    	url(r'^simple_report/$', 'userauth.views.simple_report', name='simple_report'),
      	url(r'^math_report/$', 'userauth.views.math_report', name='math_report'),
      	url(r'^writing_report/$', 'userauth.views.writing_report', name='writing_report'),
     	url(r'^reading_report/$', 'userauth.views.reading_report', name='reading_report'),
    	url(r'^advanced_report/$', 'userauth.views.advanced_report', name='advanced_report'),
    	url(r'^grade_test/$', 'userauth.views.grade_save_bubblesheet', name = 'grade_bubblesheet'),
		url(r'^test_review/$', 'userauth.views.test_review', name='test_review'),
		url(r'^dashboard/$', 'userauth.views.dashboard', name='dashboard'),
		url(r'^deleted/$', 'userauth.views.delete_test', name='delete_test'),
		url(r'^save/$', 'userauth.views.save_info', name='save'),
		url(r'^quicktips/$', 'userauth.views.quicktips', name='quicktips')
		# url(r'^sendregister/postregister/$', 'userauth.views.postregister', name='send_post'),
		)

