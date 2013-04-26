from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from players import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game_support.views.home', name='home'),
    # url(r'^game_support/', include('game_support.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',
        views.PlayerList.as_view(),
        name='player-list',
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/$',
        views.PlayerList.as_view(),
        name='player-list',
    ),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.PlayerDetail.as_view(),
        name='player-detail',
    ),
    url(r'^users/search$', views.PlayerSearch.as_view()),
    url(r'^battles/$', views.BattleList.as_view()),
    url(r'^battles/(?P<pk>[0-9]+)/$', views.BattleDetail.as_view()),
)

urlpatterns += patterns('',
    url(r'^api-auth/',
        include('rest_framework.urls',
        namespace='rest_framework')),
)
