from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

from ..iot_app import models


class DeviceModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DeviceModel
        fields = ('url', 'name')


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Device
        fields = ('url', 'serial', 'model', 'date')


class UserDeviceSerializer(serializers.HyperlinkedModelSerializer):
    device = serializers.HyperlinkedRelatedField(view_name='device-detail', queryset=models.Device.objects.all())
    metrics = serializers.SerializerMethodField()

    class Meta:
        model = models.UserDevice
        fields = ('url', 'device', 'date', 'metrics')

    def get_metrics(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('userdevicemetrics-detail', args=[obj.pk]))
