# Generated by Django 5.0.2 on 2024-02-21 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgi_app', '0002_pedido_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sgi_app.proveedor'),
        ),
    ]
