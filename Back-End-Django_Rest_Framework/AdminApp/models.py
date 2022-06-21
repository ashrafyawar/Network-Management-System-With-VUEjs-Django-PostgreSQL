from django.db import models


# Create your models here.

class Admin(models.Model):
    AdminId = models.AutoField(primary_key=True)
    AdminName = models.CharField(max_length=100)
    AdminPassword = models.CharField(max_length=100)


class DeviceInfo(models.Model):
    DeviceId = models.AutoField(primary_key=True)
    DeviceName = models.CharField(max_length=100)
    DeviceIP = models.CharField(max_length=100)
    DeviceModel = models.CharField(max_length=100)
    DeviceStatus = models.BooleanField()
    DeviceRecentLog = models.CharField(max_length=100)


class DeviceStatistics(models.Model):
    DeviceId = models.AutoField(primary_key=True)
    DeviceNetworkUpLink = models.CharField(max_length=100)
    DeviceNetworkDownLink = models.CharField(max_length=100)
    DeviceUp1 = models.CharField(max_length=100)
    DeviceDown1 = models.CharField(max_length=100)
    DeviceUp2 = models.CharField(max_length=100)
    DeviceDown2 = models.CharField(max_length=100)
    DeviceUp3 = models.CharField(max_length=100)
    DeviceDown3 = models.CharField(max_length=100)
    DeviceUp4 = models.CharField(max_length=100)
    DeviceDown4 = models.CharField(max_length=100)
    DeviceUp5 = models.CharField(max_length=100)
    DeviceDown5 = models.CharField(max_length=100)
    DeviceUp6 = models.CharField(max_length=100)
    DeviceDown6 = models.CharField(max_length=100)
    DeviceUp7 = models.CharField(max_length=100)
    DeviceDown7 = models.CharField(max_length=100)
    DeviceUp8 = models.CharField(max_length=100)
    DeviceDown8 = models.CharField(max_length=100)


class DemoRequest(models.Model):
    DemoId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=10000)
    Email = models.CharField(max_length=10000)
    Message = models.CharField(max_length=10000)


class BlockedIP(models.Model):
    IPId = models.AutoField(primary_key=True)
    IP = models.CharField(max_length=10000)


class RiskyDevice(models.Model):
    DeviceId = models.AutoField(primary_key=True)
    DeviceIP = models.CharField(max_length=100)
    DeviceType = models.CharField(max_length=100)
    DeviceActivityDesc = models.CharField(max_length=100)
    DevicePriority = models.IntegerField()