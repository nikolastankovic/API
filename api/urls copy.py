from django.conf.urls import url
from django.views.static import serve
from .views import FileView
from django.conf import settings

urlpatterns = [
  url(r'^upload/$', FileView.as_view(), name='file-upload'),
  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
  url()
]