# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ps_name', models.CharField(max_length=50)),
                ('ps_country', models.CharField(max_length=50)),
                ('ps_ticketno', models.CharField(max_length=50)),
                ('ps_gender', models.CharField(max_length=1)),
                ('ps_photo', models.CharField(max_length=100)),
                ('ps_details', models.CharField(max_length=500)),
                ('ps_role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('reg_no', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('plane_origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('onboard', models.IntegerField(default=0)),
                ('mis_date', models.DateField()),
                ('mis_location', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=1000)),
                ('plane_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='plane_no',
            field=models.ForeignKey(to='planeInfo.Plane'),
        ),
    ]
