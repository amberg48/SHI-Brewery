# Generated by Django 4.0.4 on 2022-04-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('street', models.CharField(blank=True, max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('address_3', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('county_province', models.CharField(blank=True, max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('longitude', models.CharField(blank=True, max_length=100)),
                ('latitude', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('website_url', models.CharField(blank=True, max_length=100)),
                ('updated_at', models.CharField(blank=True, max_length=100)),
                ('created_at', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]