# Generated by Django 4.1.4 on 2023-01-07 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_routes_route_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='route_available',
            field=models.BooleanField(blank=True, db_column='route_available', null=True),
        ),
    ]