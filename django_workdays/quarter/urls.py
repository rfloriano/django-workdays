from django.conf.urls import patterns, url

from .views import QuarterGoalsView


urlpatterns = patterns(
    '',
    url(r'^goals/$', QuarterGoalsView.as_view(), name='goals_quarter'),
)
