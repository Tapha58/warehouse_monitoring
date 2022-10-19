from rest_framework import serializers

from warehouse.models import Part


class TrackedPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['id', 'name', 'count']
