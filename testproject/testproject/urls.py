# encoding:utf-8
from django.conf.urls import url

from .views import Bootstrap3, Bootstrap4, Index

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^bootstrap3/$', Bootstrap3.as_view(), name="bootstrap3"),
    url(r'^bootstrap4/$', Bootstrap4.as_view(), name="bootstrap4"),
]
