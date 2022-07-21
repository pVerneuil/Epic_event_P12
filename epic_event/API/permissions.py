from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Event, Contract, Client


class IsManagementPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == "management"


class IsSaleContactPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in [SAFE_METHODS, "POST"]:
            return True
        if request.method == "PUT":
            if isinstance(obj, Client) or isinstance(obj, Contract):
                return obj.sale_contact == request.user
            if isinstance(obj, Event):
                return obj.client.sale_contact == request.user


class IsSupportContactPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "PUT" and isinstance(obj, Event):
            return obj.support_contact == request.user
