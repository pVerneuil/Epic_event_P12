from django.contrib import admin
from .models import Client, Contract, Event


@admin.register(Client)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "status", "sale_contact")


@admin.register(Contract)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("client", "sale_contact")


@admin.register(Event)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("client", "support_contact", "contract")
