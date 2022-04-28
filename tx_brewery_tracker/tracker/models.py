from django.db import models

# Database model for storing brewery information as gathered by the api
class Brewery(models.Model):
    # Fields based on output from Open Brewery API
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    address_3 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100) # Should always equal 'Texas'
    county_province = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100) # Should always equal 'United States'
    longitude = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    website_url = models.CharField(max_length=100, blank=True)
    updated_at = models.CharField(max_length=100, blank=True) 
    created_at = models.CharField(max_length=100, blank=True)