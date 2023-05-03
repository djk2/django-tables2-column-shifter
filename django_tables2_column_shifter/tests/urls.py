import django

from .views import (
    Bootstrap2,
    Bootstrap3,
    Bootstrap4,
    Bootstrap4Responsive,
    Bootstrap5,
    Bootstrap5Responsive,
)

dj_version = tuple(map(int, django.__version__.split(".")[:2]))

if dj_version >= (3, 1):
    from django.urls import re_path as url
else:
    from django.conf.urls import url


urlpatterns = [
    url(r'^bootstrap2/$', Bootstrap2.as_view(), name="bootstrap2"),
    url(r'^bootstrap3/$', Bootstrap3.as_view(), name="bootstrap3"),
    url(r'^bootstrap4/$', Bootstrap4.as_view(), name="bootstrap4"),
    url(r'^bootstrap5/$', Bootstrap5.as_view(), name="bootstrap5"),
    url(
        r'^bootstrap4responsive/$',
        Bootstrap4Responsive.as_view(),
        name="bootstrap4responsive",
    ),
    url(
        r'^bootstrap5responsive/$',
        Bootstrap5Responsive.as_view(),
        name="bootstrap5responsive",
    ),
]
