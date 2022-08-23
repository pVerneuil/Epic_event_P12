from rest_framework.permissions import BasePermission, SAFE_METHODS


class ClientsPermission(BasePermission):
    '''
    management: all permissions
    sale: safe methods, post , put if user is sale support of the client
    support: safe methods if user is support _contact for an event of the concern client
    '''
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
    """
    mamagement : all permissions
    sale : safe methods , post, put if the user is the sale_contact of the contract
    support: none
    
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.role in ["management", "sale"]
        if request.method == "POST":
            return request.user.role in ["management", "sale"]
        if request.method == "PUT":
            if request.user.role == "sale":
                return obj.sale_contact == request.user
            else:
                return request.user.role == "management"


class EventsPermission(BasePermission):
    """
    mamagement : all permissions
    sale : all permissions
    support : safe methods, put if the user is the support-contact of the event
    
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            return request.user.role in ["management", "sale"]
        if request.method == "PUT":
            if request.user.role in ["management", "sale"]:
                return True
            if request.user.role == "support":
                return obj.support_contact == request.user