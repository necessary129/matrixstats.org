"""matrix_stats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from room_stats import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stats/(?P<room_id>\![a-zA-Z0-9\.\:\_]*)/(?P<days>[0-9]*)$',
        views.get_daily_members_stats
    ),
    url(r'^room/(?P<room_id>\![a-zA-Z0-9\.\:\_\-]*)$',
        views.room_stats_view, name='room-stats',
    ),
    url(r'^$', views.list_rooms),
    url(r'^server/(?P<server>[a-zA-Z0-9\.]+)', views.list_server_stats, name='server-stats'),
    url(r'^rooms/top/', views.list_rooms_by_members_count),
    url(r'^rooms/random/', views.list_rooms_by_random),
    url(r'^rooms/cyrillic/', views.list_rooms_by_lang_ru),
    url(r'^rooms/tags/', views.list_tags),
    url(r'^rooms/tag/(?P<tag>\w+)', views.list_rooms_with_tag, name='rooms-with-tag'),

    url(r'^rooms/search/(?P<term>\w+)', views.list_rooms_by_search_term, name='rooms-with-search-term'),



]