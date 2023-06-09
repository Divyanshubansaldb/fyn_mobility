# Generated by Django 4.1.7 on 2023-03-27 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DecimalBasePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('distance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('enable', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DistanceAdditionalPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('distance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('enable', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('vechile_id', models.TextField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TimeMultiplierFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('multiple_factor', models.DecimalField(decimal_places=2, max_digits=3)),
                ('enable', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contact_info', models.TextField(max_length=10)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_time', models.IntegerField()),
                ('end_time', models.IntegerField()),
                ('distance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vechile_id', models.TextField()),
                ('dap', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pricingapi.distanceadditionalprice')),
                ('dbp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pricingapi.decimalbaseprice')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pricingapi.driver')),
                ('tmf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pricingapi.timemultiplierfactor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricingapi.user')),
            ],
        ),
    ]
