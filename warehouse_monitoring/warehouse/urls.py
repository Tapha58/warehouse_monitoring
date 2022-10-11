from django.urls import path
from rest_framework.routers import DefaultRouter

from warehouse import views
from warehouse.views import AccountViewSet

# urlpatterns = [
#     # path('tracked-part/<int:id>/', views.TrackPartApiViewId.as_view(), name="index"),
#     # path('tracked-part/', views.TrackPartApiView.as_view(), name="index"),
#     path('tracked-part/', views.TrackPartViewSet.as_view({'get': 'list'})),
#     path('tracked-part/<int:pk>/', views.TrackPartViewSet.as_view({'get': 'retrieve'}))
# ]

router = DefaultRouter()
router.register(r'tracked-part', AccountViewSet, basename='tracked-part')
urlpatterns = router.urls