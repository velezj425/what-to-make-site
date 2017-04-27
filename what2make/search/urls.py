from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^query/$', views.query, name='query'),
    url(r'^signup/$', views.signup, name='signup'),
]