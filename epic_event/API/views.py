from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Event, Contract, Client

from .serializers import (
    ClientSerializerForManagement,
    ClientSerializerForUser,
    ContractSerializerForManagement,
    ContractSerializerForUser,
    EventSerializerForManagement,
    EventSerializerForUser,
)
from .permissions import (
    IsManagementPermission,
    IsSaleContactPermission,
    IsSupportContactPermission,
)

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    
    permission_classes = [
        IsAuthenticated,
        IsManagementPermission,
        IsSaleContactPermission,
        IsSupportContactPermission
    ]
    
    def get_serializer_class(self):
        if self.request.user.role == 'management' :
            return ClientSerializerForManagement
        return ClientSerializerForUser
    