from django.conf.urls import url

from .views import Bootstrap2, BootstrapDefault

urlpatterns = [
    url(r'^bootstrap_default/$', BootstrapDefault.as_view(), name="bootstrap_default"),
    url(r'^bootstrap2/$', Bootstrap2.as_view(), name="bootstrap2"),
]
