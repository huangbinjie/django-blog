from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^r/(?P<channel>[\w]+)/$', views.index, name='index'),
]