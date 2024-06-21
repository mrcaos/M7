# Generated by Django 5.0.6 on 2024-06-21 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vehiculo",
            fields=[
                (
                    "patente",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("marca", models.CharField(max_length=20)),
                ("activo", models.BooleanField(default=False)),
                ("modelo", models.CharField(max_length=20)),
                ("year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RegistroContabilidad",
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
                ("fecha_compra", models.DateTimeField(auto_now_add=True)),
                ("valor", models.FloatField()),
                (
                    "vehiculo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contabilidad",
                        to="appcar.vehiculo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Chofer",
            fields=[
                (
                    "rut",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("activo", models.BooleanField(default=True)),
                ("creacion_registro", models.DateTimeField(auto_now_add=True)),
                (
                    "vehiculo",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="chofer",
                        to="appcar.vehiculo",
                    ),
                ),
            ],
        ),
    ]
