# encoding:utf-8
from django.conf.urls import url

from .views import (
    Bootstrap2,
    Bootstrap3,
    Bootstrap4,
    Bootstrap4_1_3,
    Bootstrap5,
    Index,
)

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^bootstrap2/$', Bootstrap2.as_view(), name="bootstrap2"),
    url(r'^bootstrap3/$', Bootstrap3.as_view(), name="bootstrap3"),
    url(r'^bootstrap4/$', Bootstrap4.as_view(), name="bootstrap4"),
    url(r'^bootstrap4_1_3/$', Bootstrap4_1_3.as_view(), name="bootstrap4_1_3"),
    url(r'^bootstrap5/$', Bootstrap5.as_view(), name="bootstrap5"),
]
