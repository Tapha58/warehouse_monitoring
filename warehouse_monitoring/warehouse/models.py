from django.db import models
from rest_framework import serializers


class TrackedPart(models.Model):
    """описание таблицы"""  # docstring # TODO: придумать описание
    name = models.CharField("название детали", max_length=255)
    count = models.IntegerField("количество")

    # def __str__(self):
    #     return "slajsvewmceijspoe"


class TrackedPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedPart
        fields = ['id', 'name', 'count']
