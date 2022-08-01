from ast import Return
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Event, Contract, Client


class ClientsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.role == "support":
                return obj.event_set.filter(support_contact=request.user)
            else:
                return request.user.role in ["management", "sale"]
        if request.method == "POST":
            return request.user.role in ["management", "sale"]
        if request.method == "PUT":
            if request.user.role == "sale":
                return obj.sale_contact == request.user
            else:
                return request.user.role == "management"


class ContractPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("ContractPermission called")
        if request.method in SAFE_METHODS:
            print("safemethod")
            return request.user.role in ["management", "sale"]
        if request.method == "POST":
            return request.user.role in ["management", "sale"]
        if request.method == "PUT":
            if request.user.role == "sale":
                return obj.sale_contact == request.user
            else:
                return request.user.role == "management"


class EventsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            print("hi")
            return request.user.role in ["management", "sale"]
        if request.method == "PUT":
            if request.user.role in ["management", "sale"]:
                return True
            if request.user.role == "support":
                return obj.support_contact == request.user


class permissionTEST(BasePermission):
    def has_object_permission(self, request, view, obj):
        return False
