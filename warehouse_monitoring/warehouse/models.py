from django.db import models
from rest_framework import serializers


class TrackedPart(models.Model):
    """описание таблицы"""  # docstring # TODO: придумать описание
    name = models.CharField("название детали", max_length=255)
    count = models.IntegerField("количество")

    # def __str__(self):
    #     return "slajsvewmceijspoe"


# class TrackedPartSerializer(serializers.Serializer):
#     id = serializers.IntegerField(label='ID', read_only=True)
#     name = serializers.CharField(max_length=255)
#     count = serializers.IntegerField()

class TrackedPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedPart
        fields = ['id', 'name', 'count']


    # def create(self, validated_data):
    #     b = TrackedPart(name=validated_data['name'], count=validated_data['count'])
    #     b.save()
    #     return b
    #     #return TrackedPart.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data['name']
    #     instance.count = validated_data['count']
    #     instance.save()
    #     # updating
    #     return instance