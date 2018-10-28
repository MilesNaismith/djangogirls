from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.shopping, name='shopping'),
]