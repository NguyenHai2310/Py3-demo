from django.conf.urls import include, url
from py3.apps.service.views import (
    ServiceListView, CategoryListView, ServiceListViewByStore
)

urlpatterns = [
    url(r'^servicelist/$', ServiceListView.as_view()),
    url(r'^servicelist/(?P<category>.+)/(?P<service>.+)/$', ServiceListView.as_view()),
    url(r'^servicelist/(?P<category>.+)/$', ServiceListView.as_view()),
    url(r'^category/$',CategoryListView.as_view()),
    url(r'^category/(?P<category>.+)/$', CategoryListView.as_view() ),
    url(r'^categories/$',CategoryListView.as_view()),
    url(r'^store/(?P<store>.+)/$', ServiceListViewByStore.as_view()),
    url(r'^stores/(?P<store>.+)/$', ServiceListViewByStore.as_view()),
    url(r'^stores/$', ServiceListViewByStore.as_view()),
]
