from django.urls import re_path, path
from AdminApp import views

urlpatterns = [
    path('', views.adminApi, name='admin'),
    re_path(r'^admins$', views.adminApi, name='admin'),
    re_path(r'^admins/([0-9])$', views.adminApi),
    re_path(r'^devicelist$', views.deviceApi, name='device'),
    re_path(r'^devicestatistics$', views.deviceStatisticsApi, name='deviceStatistics'),
    re_path(r'^submitadmin$', views.adminApi, name='device'),
    re_path(r'^authenticate-user$', views.authenticate, name='device'),
    re_path(r'^postdemorequest$', views.demoRequest, name='device'),
    re_path(r'^postdevice$', views.deviceApi, name='device'),
    re_path(r'^riskydevice$', views.riskyDeviceApi, name='device'),
    re_path(r'^blockedip$', views.blockedIPApi, name='device'),

]
