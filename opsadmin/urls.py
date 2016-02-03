from django.conf.urls import url
from opsadmin import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name_id>[0-9]+)/$', views.detail, name='detail'),
]