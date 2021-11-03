from rest_framework import routers, urlpatterns
from .api import CourseViewSet

router = routers.DefaultRouter()
router.register('api/courses',CourseViewSet,'courses')

urlpatterns = router.urls 