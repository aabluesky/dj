from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.home,name='home'),
	url(r'^(?P<id>\d+)/$',views.detail,name='detail'),
	url(r'^archives/$',views.archives,name='archives'),
	url(r'^aboutme/$',views.about_me,name='about_me'),
	url(r'^tag(?P<tag>\w+)/$',views.search_tag, name = 'search_tag'),
	url(r'^search/$',views.blog_search, name = 'search'),
]
