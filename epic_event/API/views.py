from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
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
    ClientsPermission,
    ContractPermission,
    EventsPermission,
    permissionTEST,
    
)

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    
    permission_classes = [
        IsAuthenticated,
        ClientsPermission,
    ]
    def create(self, request):
        self.check_object_permissions(self.request, Client)
        if self.request.user.role == 'management' :
            serializer = ClientSerializerForManagement(context={"request": request}, data=request.data)
        else :
            serializer = ClientSerializerForManagement(context={"request": request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.request.user.role == 'management' :
            return ClientSerializerForManagement
        return ClientSerializerForUser


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    
    permission_classes = [
        IsAuthenticated,
        ContractPermission
    ]
    def create(self, request):
        self.check_object_permissions(self.request, Contract)
        if self.request.user.role == 'management' :
            serializer = ContractSerializerForManagement(context={"request": request}, data=request.data)
        else :
            serializer = ContractSerializerForManagement(context={"request": request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.request.user.role == 'management' :
            return ContractSerializerForManagement
        return ContractSerializerForUser

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    
    permission_classes = [
        IsAuthenticated,
        EventsPermission,
    ]
    
    def create(self, request):
        self.check_object_permissions(self.request, Event)
        if self.request.user.role == 'management' :
            serializer = EventSerializerForManagement(context={"request": request}, data=request.data)
        else :
            serializer = EventSerializerForManagement(context={"request": request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_serializer_class(self):
        if self.request.user.role == 'management' :
            return EventSerializerForManagement
        return EventSerializerForUser
    