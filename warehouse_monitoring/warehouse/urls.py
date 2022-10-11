from rest_framework.routers import DefaultRouter

from warehouse.views import TrackedPartViewSet


router = DefaultRouter()
router.register(r'tracked-part', TrackedPartViewSet, basename='tracked-part')
urlpatterns = router.urls
