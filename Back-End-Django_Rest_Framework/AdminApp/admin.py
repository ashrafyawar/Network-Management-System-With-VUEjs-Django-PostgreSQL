from django.contrib import admin
from .models import Admin, DemoRequest, DeviceStatistics
from . models import DeviceInfo

admin.site.register(Admin)
admin.site.register(DeviceInfo)
admin.site.register(DemoRequest)
admin.site.register(DeviceStatistics)
