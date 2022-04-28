from django.db import models

# Database model for storing brewery information as gathered by the api
class Brewery(models.Model):
    # Fields based on output from Open Brewery API
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=255, null=True)
    address_2 = models.CharField(max_length=255, null=True)
    address_3 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True) # Should always equal 'Texas'
    county_province = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True) # Should always equal 'United States'
    longitude = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    website_url = models.CharField(max_length=100, null=True)
    updated_at = models.CharField(max_length=100, null=True) 
    created_at = models.CharField(max_length=100, null=True)

    def format_Phone(self):
        phone = self.phone
        if phone:
            return "(" + phone[0:3] + ") " + phone[3:6] + "-" + phone[6:]
        else:
            return None

    def format_Address(self):
        formatAddr = ""
        if self.street:
            formatAddr += self.street + ", "
            if self.city:
                formatAddr += self.city + ", "
                if self.state:
                    formatAddr += self.state + ", "
                    if self.country:
                        formatAddr += self.country
        return formatAddr