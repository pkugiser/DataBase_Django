from django.conf.urls import url
from . import views
app_name = 'main'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^map/$', views.map, name='map'),
	url(r'^test/$', views.test, name='test'),
	url(r'^poirst/$', views.poirst, name='poirst'),
	url(r'^result/$', views.result, name='result'),
	url(r'^dheatmap/$', views.dheatmap, name='dheatmap'),
	url(r'^cheatmap/$', views.cheatmap, name='cheatmap'),
	url(r'^category/$', views.category, name='category'),
	url(r'^userinfo/(?P<uid>\d+)/$', views.userinfo, name='userinfo'),
	url(r'^EmotionAnalysis/$', views.EmotionAnalysis, name='emotionanalysis'),
	url(r'^DaypartsAnalysis/$', views.DaypartsAnalysis, name='daypartsanalysis'),
	url(r'^POIAnalysis/$', views.POIAnalysis, name='poianalysis'),
	url(r'^RegionAnalysis/$', views.RegionAnalysis, name='regionanalysis'),
	url(r'^EmotionAnalysis/(?P<uid>\d+)/$', views.ea, name='ea'),
	url(r'^DaypartsAnalysis/(?P<uid>\d+)/$', views.da, name='da'),
	url(r'^POIAnalysis/(?P<uid>\d+)/$', views.pa, name='pa'),
	url(r'^RegionAnalysis/(?P<uid>\d+)/$', views.ra, name='ra'),
]