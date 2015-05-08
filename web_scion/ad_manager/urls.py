# External packages
from django.conf.urls import patterns, url

# SCION
from ad_manager import views


urlpatterns = patterns(
    '',
    url(r'^isds/$',
        views.ISDListView.as_view(), name='list_isds'),
    url(r'^isds/(?P<pk>\d+)/$',
        views.ISDDetailView.as_view(), name='isd_detail'),
    url(r'^ads/(?P<pk>\d+)/$',
        views.ADDetailView.as_view(), name='ad_detail'),
    url(r'^ads/(?P<pk>\d+)/#!topology$',
        views.ADDetailView.as_view(), name='ad_detail_topology'),
    url(r'^ads/(?P<pk>\d+)/#!updates$',
        views.ADDetailView.as_view(), name='ad_detail_updates'),
    url(r'^ads/(?P<pk>\d+)/get_status$',
        views.get_ad_status, name='ad_status'),
    url(r'^ads/(?P<pk>\d+)/compare_remote_topology$',
        views.compare_remote_topology, name='compare_topology'),
    url(r'^ads/(?P<pk>\d+)/update_topology$',
        views.update_topology, name='update_topology'),
    url(r'^ads/(?P<pk>\d+)/update_action$',
        views.update_action, name='update_action'),
    url(r'^ads/(?P<pk>\d+)/refresh_versions$',
        views.refresh_versions, name='refresh_versions'),
    url(r'^ads/(?P<pk>\d+)/connect_new_ad$',
        views.connect_new_ad, name='connect_new_ad'),
)