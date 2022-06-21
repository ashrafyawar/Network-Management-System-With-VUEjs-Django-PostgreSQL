import datetime

from django.utils import timezone
from rest_framework.decorators import api_view

from AdminApp.models import Admin, DeviceInfo, DemoRequest, DeviceStatistics, RiskyDevice, BlockedIP
from AdminApp.serializers import AdminSerializer, DeviceInfoSerializer, DemoRequestSerializer, \
    DeviceStatisticsSerializer, RiskyDeviceSerializer, BlockedIPSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import smtplib
from datetime import datetime

import socket
from email.message import EmailMessage


# Create your views here.

@csrf_exempt
def authenticate(request, id=0):  # get user, post user
    if request.method == 'GET':
        admins = Admin.objects.all()
        admin_serializer = AdminSerializer(admins, many=True)
        return JsonResponse(admin_serializer.data, safe=False)
    elif request.method == 'POST':
        pass


@csrf_exempt
def adminApi(request, id=0):  # get admin list, post admin
    if request.method == 'GET':  # authenticate user
        return JsonResponse("Null", safe=False)
    elif request.method == 'POST':
        admin_data = JSONParser().parse(request)
        admin_serializer = AdminSerializer(data=admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed To Add", safe=False)
    elif request.method == 'PUT':
        admin_data = JSONParser().parse(request)
        admin = Admin.objects.get(AdminId=admin_data['AdminId'])
        admin_serializer = AdminSerializer(admin, data=admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        else:
            return JsonResponse("Update Failed", safe=False)
    elif request.method == 'DELETE':
        admin = Admin.objects.get(AdminId=id)
        admin.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def deviceApi(request, id=0):  # get devices list
    if request.method == 'GET':
        devices = DeviceInfo.objects.all()
        devices_serializer = DeviceInfoSerializer(devices, many=True)
        return JsonResponse(devices_serializer.data, safe=False)
    elif request.method == 'POST':
        device_data = JSONParser().parse(request)
        device_serializer = DeviceInfoSerializer(data=device_data)
        if device_serializer.is_valid():
            device_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed To Add", safe=False)


@csrf_exempt
def riskyDeviceApi(request, id=0):  # get risky devices list
    if request.method == 'GET':
        riskyDevices = RiskyDevice.objects.all()
        risky_devices_serializer = RiskyDeviceSerializer(riskyDevices, many=True)
        return JsonResponse(risky_devices_serializer.data, safe=False)
    elif request.method == 'POST':
        risky_device_data = JSONParser().parse(request)
        risky_device_serializer = RiskyDeviceSerializer(data=risky_device_data)
        if risky_device_serializer.is_valid():
            risky_device_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed To Add", safe=False)
    elif request.method == 'DELETE':
        pass


@csrf_exempt
def blockedIPApi(request, id=0):  # get risky devices list
    if request.method == 'GET':
        blockedIPs = BlockedIP.objects.all()
        blockedIPsSerializer = BlockedIPSerializer(blockedIPs, many=True)
        return JsonResponse(blockedIPsSerializer.data, safe=False)
    elif request.method == 'POST':
        blockedIpData = JSONParser().parse(request)
        blockedIpSerializer = BlockedIPSerializer(data=blockedIpData)
        if blockedIpSerializer.is_valid():
            blockedIpSerializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed To Add", safe=False)


@csrf_exempt
def deviceStatisticsApi(request, id=0):  # get devices list
    if request.method == 'GET':
        deviceStatistics = DeviceStatistics.objects.all()
        deviceStatistics_serializer = DeviceStatisticsSerializer(deviceStatistics, many=True)
        return JsonResponse(deviceStatistics_serializer.data, safe=False)
    elif request.method == 'POST':
        pass


@csrf_exempt
def demoRequest(request, id=0):  # post get demo request, sent email,
    if request.method == 'GET':
        demoRequests = DemoRequest.objects.all()
        demoRequestsSerializer = DemoRequestSerializer(demoRequests, many=True)
        return JsonResponse(demoRequestsSerializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        dataSerializer = DemoRequestSerializer(data=data)
        if dataSerializer.is_valid():
            dataSerializer.save()
            # msg = EmailMessage()
            # msg['Subject'] = 'Demo Request'
            # msg['From'] = dataSerializer.data['Name']
            # msg['To'] = 'emailhere'
            # msg.set_content(
            #     'You Have A Demo Request From: ' + dataSerializer.data['Name'] +
            #     '\nWith Email: ' + dataSerializer.data['Email'] +
            #     '\nWith Content: ' + dataSerializer.data['Message'])
            # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            # server.login('emailhere', 'passwordhere')
            # server.send_message(msg)
            # server.quit()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed To Add", safe=False)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
