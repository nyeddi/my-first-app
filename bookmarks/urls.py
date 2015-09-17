from django.conf.urls import url, include

from . import views

'''urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<object_id>\d+)/$',
        view='bookmark_detail',
        name='bookmark_detail',
    ),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 
        view='bookmark_archive_day',
        name='bookmark_archive_day',
    ),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
        view='bookmark_archive_month',
        name='bookmark_archive_month',
    ),
    url(r'^(?P<year>\d{4})/$',
        view='bookmark_archive_year',
        name='bookmark_archive_year',
    ),
    url(r'^$',
        views.BookmarkListView.as_view(),
        name='bookmark_index',
    ),
]'''

urlpatterns = [
    url(r'^$',
        views.BookmarkListView.as_view(),
        name='bookmark_index',
    ),
]