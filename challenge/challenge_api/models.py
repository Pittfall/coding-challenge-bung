import uuid
from django.db import models
from django.utils import timezone


class AreaUnit(models.TextChoices):
    SQUARE_FEET = 'SqFt', 'Square Feet'



class HomeType(models.TextChoices):
    SINGLE_FAMILY = 'SingleFamily', 'Single Family'
    VACANT_RESIDENTIAL_LAND = 'VacantResidentialLand', 'Vacant Residential Land'
    MISCELLANEOUS = 'Miscellaneous', 'Miscellaneous'
    MULTI_FAMILY_2_TO_4 = 'MultiFamily2To4', 'Multi-Family (2 to 4 Units)'
    CONDOMINIUM = 'Condominium', 'Condominium'
    APARTMENT = 'Apartment', 'Apartment'
    DUPLEX = 'Duplex', 'Duplex'
    OTHER = 'Other', 'Other'


class ZillowListing(models.Model):
    '''House model representation.'''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    zillow_id = models.IntegerField(null=True, blank=True)
    link = models.URLField()

    area_unit = models.CharField(
        max_length=32,
        choices=AreaUnit.choices,
        null=True,
        help_text='The unit of area measurement. ex. sqft'
    )
    bathrooms = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    bedrooms = models.IntegerField(null=True, blank=True)
    home_size = models.IntegerField(null=True, blank=True)
    home_type = models.CharField(max_length=64, choices=HomeType.choices, default=HomeType.OTHER)
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    property_size = models.IntegerField(null=True, blank=True)
    rent_price = models.IntegerField(null=True, blank=True)
    tax_value = models.IntegerField(null=True, blank=True)
    tax_year = models.IntegerField(null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)

    rentzestimate_amount = models.IntegerField(null=True, blank=True)
    rentzestimate_last_updated = models.DateField(null=True, blank=True)
    zestimate_amount = models.IntegerField(null=True, blank=True)
    zestimate_last_updated = models.DateField(null=True, blank=True)

    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)

    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.zillow_id} - {self.street}, {self.city}, {self.state} {self.zipcode or ''}"