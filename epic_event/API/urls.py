from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ContractViewSet, EventViewSet

router = DefaultRouter()

router.register(r"clients", ClientViewSet, basename="clients")
router.register(r"contracts", ContractViewSet, basename="contracts")
router.register(r"events", EventViewSet, basename="events")

urlpatterns = [
    path("", include(router.urls)),
]
