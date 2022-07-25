from posixpath import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ContractViewSet, EventViewSet

router = DefaultRouter()

router.register(r'clients',ClientViewSet,basename='clients')
router.register(r'Contracts',ClientViewSet,basename='contracts')
router.register(r'events',ClientViewSet,basename='events')

urlpatterns = [
	path("", include(router.urls)),
]