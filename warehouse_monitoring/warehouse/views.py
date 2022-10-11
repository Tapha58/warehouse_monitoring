from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from warehouse.models import TrackedPart, TrackedPartSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = TrackedPart.objects.all()
    serializer_class = TrackedPartSerializer
    lookup_field = "cccc"
    # permission_classes = [IsAccountAdminOrReadOnly]
    # def list(self, request):
    #     # queryset = TrackedPart.objects.all()
    #     serializer = TrackedPartSerializer(self.queryset, many=True)
    #     return Response(serializer.data)



# class TrackPartViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = TrackedPart.objects.all()
#         serializer = TrackedPartSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = TrackedPart.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = TrackedPartSerializer(user)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = TrackedPartSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         instance = serializer.save()
#         serializer = TrackedPartSerializer(instance)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         part = get_object_or_404(TrackedPart, pk=pk)
#         serializer = TrackedPartSerializer(part, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         instance = serializer.save()
#         serializer = TrackedPartSerializer(instance)
#         return Response(serializer.data)


# class TrackPartApiView(APIView):
#     def get(self, request):
#         queryset = TrackedPart.objects.all()
#         serializer = TrackedPartSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request):
#         serializer = TrackedPartSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         instance = serializer.save()
#         serializer = TrackedPartSerializer(instance)
#         return Response(serializer.data)
#
#
# class TrackPartApiViewId(APIView):
#     def get(self, request, id):
#         part = get_object_or_404(TrackedPart, pk=id)
#         serializer = TrackedPartSerializer(part)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         part = get_object_or_404(TrackedPart, pk=id)
#         serializer = TrackedPartSerializer(part, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         instance = serializer.save()
#         serializer = TrackedPartSerializer(instance)
#         return Response(serializer.data)
#
#     def delete(self, request, id):
#         try:
#             TrackedPart.objects.filter(pk=id).delete()
#             return Response('Delete')
#         except TrackedPart.DoesNotExist as e:
#             return Response(None, status=404)

