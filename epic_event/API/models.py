from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=200, null=False)
    phone = models.CharField(max_length=20, null=False)
    mobile = models.CharField(max_length=20, null=False)
    company_name = models.CharField(max_length=250, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sale_contact = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
class Contract(models.Model):
    sale_contact = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField(null=True, blank=True)

class Event(models.Model):
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    event_status = models.ForeignKey(Contract,to_field='status')
    attendees = models.IntegerField(default=0)
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=10000, blank=True)
