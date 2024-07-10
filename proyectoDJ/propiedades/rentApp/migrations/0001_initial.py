# Generated by Django 5.0.6 on 2024-06-28 19:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Region",
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
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tipo_inmueble",
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
                ("nombre", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Tipo_usuario",
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
                ("nombre", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="Comuna",
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
                ("nombre", models.CharField(max_length=100)),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rentApp.region"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "rut",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("nombres", models.CharField(max_length=50)),
                ("apellidos", models.CharField(max_length=50)),
                ("direccion", models.CharField(max_length=50)),
                ("telefono", models.CharField(max_length=50)),
                ("correo", models.CharField(max_length=50)),
                (
                    "tipo_usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rentApp.tipo_usuario",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inmueble",
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
                ("nombre", models.CharField(max_length=50)),
                ("descripcion", models.TextField()),
                ("m2_construidos", models.FloatField()),
                ("m2_terreno", models.FloatField()),
                ("num_estacionamiento", models.IntegerField(default=0)),
                ("num_habitaciones", models.IntegerField(default=0)),
                ("num_banios", models.IntegerField(default=0)),
                ("direccion", models.CharField(max_length=50)),
                ("precio_mensual", models.FloatField()),
                ("arrendada", models.BooleanField(default=False)),
                (
                    "arrendador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "comuna",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rentApp.comuna"
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rentApp.region"
                    ),
                ),
                (
                    "tipo_inmueble",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rentApp.tipo_inmueble",
                    ),
                ),
                (
                    "arrendatario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rentApp.usuario",
                    ),
                ),
            ],
        ),
    ]
