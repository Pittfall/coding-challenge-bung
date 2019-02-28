from django.db import models


class House(models.Model):
    """House model representation."""

    area_unit = models.CharField(max_length=255)
    bathrooms = models.FloatField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    home_size = models.IntegerField(null=True, blank=True)
    home_type = models.CharField(max_length=100)
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price = models.IntegerField(null=True, blank=True)
    link = models.URLField()
    price = models.IntegerField(null=True, blank=True)
    property_size = models.IntegerField(null=True, blank=True)
    rent_price = models.IntegerField(null=True, blank=True)
    rentzestimate_amount = models.IntegerField(null=True, blank=True)
    rentzestimate_last_updated = models.DateField(null=True, blank=True)
    tax_value = models.IntegerField(null=True, blank=True)
    tax_year = models.IntegerField(null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)
    zestimate_amount = models.IntegerField(null=True, blank=True)
    zestimate_last_updated = models.DateField(null=True, blank=True)
    zillow_id = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField(null=True, blank=True)
