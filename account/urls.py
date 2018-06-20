from django.conf.urls import url

from account.views import *
from . import views

urlpatterns = [

 	url(r'^$', views.get_info, name='index'),
    url(r'^account/receit/$', views.receit, name='receit'),
    url(r'^(?P<pk>\d+)/$', AccountDV.as_view(), name='detail'),

    ]
