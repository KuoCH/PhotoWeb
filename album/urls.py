from django.conf.urls import patterns, url

from album import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<picture_id>\d+)/$', views.detail, name='detail'),
    url(r'^pictures/$', views.picture_list),
    url(r'^pictures/(?P<pk>[0-9]+)/$', views.picture_detail),
    url(r'^comments/$', views.comment_list),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.comment_detail),
)
