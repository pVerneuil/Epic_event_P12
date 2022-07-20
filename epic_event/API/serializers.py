from dataclasses import field
from rest_framework import serializers
from .models import Event, Contract, Client

#https://stackoverflow.com/questions/41366832/django-rest-api-make-field-read-only-for-certain-permission-level

class ClientSerializerForManagement(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'first_name', 
            'last_name', 
            'status', 
            'email', 
            'phone', 
            'mobile', 
            'company_name', 
            'date_created', 
            'date_updated'
            )
        read_only_fields = ('sale_contact')

class ContractSerializerForManagement(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class ContractSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = (
            'client',
            'date_created', 
            'date_updated', 
            'status', 
            'amount', 
            'payment_due'
		)
        read_only_fields = 	('sale_contact')

class EventSerializerForManagement(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
		'client',
		'date_created',
		'date_updated',
		'contract',
		'attendees',
		'event_date',
		'notes'
		)
        read_only_fields = 	('support_contact')