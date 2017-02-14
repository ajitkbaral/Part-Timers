from django.conf.urls import url
from . import views

app_name = 'work'

urlpatterns = [
	url(r'^login/$', views.login_user, name='login_user'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logout_user, name='logout_user'),
	url(r'^$', views.index, name='index'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^response/$', views.response, name='response'),
	url(r'^request_from-(?P<user_id>\d+)-for((?P<work_id>\d+))$', views.request, name='request'),
	url(r'^new-work-post/$', views.new_work_post, name='new-work-post'),
]