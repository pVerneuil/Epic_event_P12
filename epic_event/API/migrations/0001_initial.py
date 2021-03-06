# Generated by Django 4.0.6 on 2022-07-19 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
                (
                    "status",
                    models.CharField(
                        choices=[("potential", "potential"), ("active", "active")],
                        default="potential",
                        max_length=9,
                    ),
                ),
                ("email", models.EmailField(max_length=200)),
                ("phone", models.CharField(max_length=20)),
                ("mobile", models.CharField(max_length=20)),
                ("company_name", models.CharField(max_length=250)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=False)),
                ("amount", models.FloatField()),
                ("payment_due", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("attendees", models.IntegerField(default=0)),
                ("event_date", models.DateTimeField()),
                ("notes", models.TextField(blank=True, max_length=10000)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="API.client"
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="API.contract",
                    ),
                ),
            ],
        ),
    ]
