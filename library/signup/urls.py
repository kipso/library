from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$',views.register,name='register'),
	url(r'^login/',auth_views.login,{'template_name' : 'login.html'},name='login'),
	url(r'^logout/',auth_views.logout,{'template_name' : 'logout.html'},name='logout'),
	url(r'^profile/',views.profile,name='profile'),
	url(r'^about/',views.about,name='about'),
	url(r'^lend/',views.lend,name='lend'),
	url(r'^return/',views.returned,name='return'),
]