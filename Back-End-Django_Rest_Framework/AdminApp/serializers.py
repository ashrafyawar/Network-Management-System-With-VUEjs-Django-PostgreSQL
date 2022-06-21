from rest_framework import serializers
from AdminApp.models import Admin, DeviceInfo, DemoRequest, DeviceStatistics, BlockedIP, RiskyDevice


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('AdminId', 'AdminName', 'AdminPassword')


class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = ('DeviceId', 'DeviceName', 'DeviceIP', 'DeviceModel', 'DeviceStatus','DeviceRecentLog')


class DeviceStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatistics
        fields = ('DeviceId', 'DeviceNetworkUpLink', 'DeviceNetworkDownLink', 'DeviceUp1', 'DeviceDown1',
                  'DeviceUp2', 'DeviceDown2', 'DeviceUp3', 'DeviceDown3', 'DeviceUp4', 'DeviceDown4',
                  'DeviceUp5', 'DeviceDown5', 'DeviceUp6', 'DeviceDown6', 'DeviceUp7', 'DeviceDown7', 'DeviceUp8', 'DeviceDown8')


class DemoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoRequest
        fields = ('DemoId', 'Name', 'Email', 'Message')


class BlockedIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedIP
        fields = ('IPId', 'IP')


class RiskyDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskyDevice
        fields = ('DeviceId', 'DeviceIP', 'DeviceType', 'DeviceActivityDesc', 'DevicePriority')