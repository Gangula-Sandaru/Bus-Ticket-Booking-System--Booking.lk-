# Generated by Django 4.1 on 2022-10-21 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_postdestinations_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='busdetails',
            name='route_date',
            field=models.DateField(blank=True, db_column='routeDate', null=True),
        ),
        migrations.AlterField(
            model_name='routes',
            name='bus_data_id',
            field=models.ForeignKey(db_column='busDataId', on_delete=django.db.models.deletion.CASCADE, to='main.busdetails'),
        ),
    ]