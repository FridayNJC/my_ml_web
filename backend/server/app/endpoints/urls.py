from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from app.endpoints.views import EndpointViewSet
from app.endpoints.views import MLAlgorithmViewSet
from app.endpoints.views import MLAlgorithmStatusViewSet
from app.endpoints.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
]
