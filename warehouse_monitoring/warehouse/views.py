from django.http import HttpResponse
from rest_framework import viewsets

from warehouse.models import Part
from warehouse.serializers import TrackedPartSerializer


class TrackedPartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = TrackedPartSerializer


def index(request):
    return HttpResponse('Hello')
