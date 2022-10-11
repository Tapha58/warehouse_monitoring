from rest_framework import viewsets

from warehouse.models import TrackedPart, TrackedPartSerializer


class TrackedPartViewSet(viewsets.ModelViewSet):
    queryset = TrackedPart.objects.all()
    serializer_class = TrackedPartSerializer
