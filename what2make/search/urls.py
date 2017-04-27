from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^query/$', views.query, name='query'),
    url(r'^(?P<profile_id>[0-9]+)/result/$', views.result, name='result'),
    url(r'^signup/$', views.signup, name='signup'),
]