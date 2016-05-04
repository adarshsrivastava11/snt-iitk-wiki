from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import *
from wiki.views import *

urlpatterns = patterns('',

	(r'^$', main_page),
	(r'^signup/$', signup_page),
	(r'^login/$', login_page),
	(r'^logout/$', logout_page),
	(r'^clubs/$', clubs_page),
	(r'^programmingclub/$', programming_club),
	(r'^(?P<team_name>[a-zA-Z]+)/dashboard/$', dashboard),
	(r'^(?P<team_name>[a-zA-Z]+)/team/$', team_profile),
	(r'^(?P<team_name>[a-zA-Z]+)/report/$', report_upload),
	
    (r'^admin/', include(admin.site.urls)),
)
