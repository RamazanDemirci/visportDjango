from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('seasons/', views.Seasons.as_view()),
    path('standings/', views.StandingTable.as_view()),
    path('standings/<int:id>', views.StandingDetail.as_view()),
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:id>', views.TeamDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
