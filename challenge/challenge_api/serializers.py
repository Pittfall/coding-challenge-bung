from rest_framework import serializers

from . import models


class ZillowListingSerializer(serializers.ModelSerializer):
    '''
    A serializer for ZillowListing model.
    '''

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

    def validate_year_built(self, value):
        if value and value > 2025:
            raise serializers.ValidationError("Year built cannot be in the future.")
        return value

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
