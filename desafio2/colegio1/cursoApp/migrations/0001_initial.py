# Generated by Django 5.0.6 on 2024-06-22 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "codigo",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("version", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Estudiante",
            fields=[
                (
                    "rut",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellidos", models.CharField(max_length=50)),
                ("fecha_nacimiento", models.DateTimeField()),
                ("activo", models.BooleanField(default=False)),
                ("creacion_registro", models.DateTimeField(auto_now_add=True)),
                ("modificacion_registro", models.DateTimeField(auto_now=True)),
                ("creado_por", models.CharField(max_length=50)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="estudiantes",
                        to="cursoApp.curso",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Direccion",
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
                ("calle", models.CharField(max_length=50)),
                ("numero", models.CharField(max_length=10)),
                ("depto", models.CharField(max_length=10, null=True)),
                ("comuna", models.CharField(max_length=50)),
                ("ciudad", models.CharField(max_length=50)),
                ("region", models.CharField(max_length=50)),
                (
                    "estudiante",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="direccion",
                        to="cursoApp.estudiante",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "rut",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellidos", models.CharField(max_length=50)),
                ("activo", models.BooleanField(default=False)),
                ("creado_por", models.CharField(max_length=50)),
                ("creacion_registro", models.DateTimeField(auto_now_add=True)),
                ("modificacion_registro", models.DateTimeField(auto_now=True)),
                (
                    "curso",
                    models.ManyToManyField(
                        related_name="profesores", to="cursoApp.curso"
                    ),
                ),
            ],
        ),
    ]
