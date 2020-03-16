from django.conf.urls import url
from django.urls import path
from django.views.static import serve
from .views import send_json,search_movie,search_episodes
from django.conf import settings

urlpatterns = [
  path('sendjson/',send_json,name='send-json'),
  path('searchmovie',search_movie,name='search-movie'),
  path('searchepisodes',search_episodes,name='search-episodes'),
 # url(r'^upload/$', FileView.as_view(), name='file-upload'),
  #url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})

]