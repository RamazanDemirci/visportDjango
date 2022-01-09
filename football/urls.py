from django.conf.urls import url
from . import views 
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^api/leagues$', views.league_list, name='league_list'),
    url(r'^api/league/(?P<pk>\w+)$', views.league_detail, name='league_detail'),
    url(r'^api/matches$', views.matches), 
    url(r'^api/persons$', views.persons),
    url(r'^api/upload/logo$', views.logos),
    url(r'^api/download/logo$', views.logos),
    
    url(r'^api/seasons$', views.seasons),
    url(r'^api/teams$', views.teams),
    url(r'^api/standing$', views.standing),
    url(r'^api/standing_all$', views.standing_all),
    url(r'^api/fixture$', views.fixture),
    url(r'^api/match_exist$', views.match_exist),
    url(r'^api/matchByHost$', views.matchByHost),
    url(r'^$', schema_view),

    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published)
]
