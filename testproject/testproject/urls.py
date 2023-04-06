# encoding:utf-8

from django.urls import re_path

from .views import (
    Bootstrap2,
    Bootstrap3,
    Bootstrap4,
    Bootstrap4_1_3,
    Bootstrap5,
    Index,
)

urlpatterns = [
    re_path(r'^$', Index.as_view(), name="index"),
    re_path(r'^bootstrap2/$', Bootstrap2.as_view(), name="bootstrap2"),
    re_path(r'^bootstrap3/$', Bootstrap3.as_view(), name="bootstrap3"),
    re_path(r'^bootstrap4/$', Bootstrap4.as_view(), name="bootstrap4"),
    re_path(r'^bootstrap4_1_3/$', Bootstrap4_1_3.as_view(), name="bootstrap4_1_3"),
    re_path(r'^bootstrap5/$', Bootstrap5.as_view(), name="bootstrap5"),
]
