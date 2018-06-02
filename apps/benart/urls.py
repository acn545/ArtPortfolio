from django.conf.urls import url
from . import views           
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

]