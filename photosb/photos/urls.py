from rest_framework import routers
from .api import PhotoViewSet

router = routers.DefaultRouter()
router.register('api/photos', PhotoViewSet, 'photos')

urlpatterns = router.urls