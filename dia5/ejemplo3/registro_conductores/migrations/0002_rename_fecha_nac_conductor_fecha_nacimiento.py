# Generated by Django 5.0.6 on 2024-06-20 19:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("registro_conductores", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="conductor",
            old_name="fecha_nac",
            new_name="fecha_nacimiento",
        ),
    ]