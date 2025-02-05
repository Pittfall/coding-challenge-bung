from rest_framework import serializers

from . import models


class ZillowListingSerializer(serializers.ModelSerializer):
    '''
    A serializer for ZillowListing model.
    '''

    class Meta:
        model = models.ZillowListing
        fields = [
            'id',
            'zillow_id',
            'link',
            'area_unit',
            'bathrooms',
            'bedrooms',
            'home_size',
            'home_type',
            'last_sold_date',
            'last_sold_price',
            'price',
            'property_size',
            'rent_price',
            'tax_value',
            'tax_year',
            'year_built',
            'rentzestimate_amount',
            'rentzestimate_last_updated',
            'zestimate_amount',
            'zestimate_last_updated',
            'street',
            'city',
            'state',
            'zipcode',
        ]
