# Generated by Django 5.1.3 on 2024-11-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principios_activos', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='principioactivo',
            constraint=models.UniqueConstraint(fields=('nombre', 'concentracion'), name='unique_compocicion'),
        ),
    ]
