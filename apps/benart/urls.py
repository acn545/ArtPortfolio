from django.conf.urls import url
from . import views
from django.conf import settings  
from django.conf.urls.static import static         
urlpatterns = [
    url(r'^$', views.main),
    url(r'^home$', views.main),
    url(r'^contact$', views.contact),
    url(r'^about$', views.about),
    url(r'^paintings$', views.paint),
    url(r'^drawings$', views.draw),
    url(r'^3dart$', views.threed),
    url(r'^gameart$', views.game),
    url(r'^login$', views.login),
    url(r'^registration$', views.registration),
    url(r'^register$', views.register),
    url(r'^validate_login$', views.validate_login),
    url(r'^dashboard$', views.simple_upload),
    url(r'^blog$', views.blog),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)