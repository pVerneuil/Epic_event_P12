from django.contrib import admin
from .models import Client, Contract, Event


@admin.register(Client)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "status", "sale_contact")


@admin.register(Contract)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "sale_contact", "date_created")


@admin.register(Event)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "support_contact", "contract")
