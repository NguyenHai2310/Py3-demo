from django.conf.urls import include, url
from py3.apps.service.views import (
    ServiceListView, CategoryListView
)

urlpatterns = [
    url(r'^servicelist/$', ServiceListView.as_view()),
    url(r'^servicelist/(?P<category>.+)/(?P<service>.+)/$', ServiceListView.as_view()),
    url(r'^servicelist/(?P<category>.+)/$', ServiceListView.as_view()),
    url(r'^categories/$',CategoryListView.as_view()),
]
