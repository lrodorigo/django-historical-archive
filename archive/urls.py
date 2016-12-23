from django.conf.urls import url

from . import views

appname = 'archive'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view-item/$', views.index2, name='index2'),
]

