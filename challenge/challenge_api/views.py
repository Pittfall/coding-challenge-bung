from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models


class ZillowListingViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    retrieve:

    Retrieve details of a specific Zillow listing by its ID.

    retrieve_response:

    HTTP 200 OK

    {
        "id": "1db4e4ae-b969-42e7-85e9-bdf56c9c4d87",
        "zillow_id": 12345678,
        "link": "https://www.zillow.com/homedetails/12345678_zpid/",
        "area_unit": "SqFt",
        "bathrooms": 2.5,
        "bedrooms": 4,
        "home_size": 2500,
        "home_type": "SingleFamily",
        "last_sold_date": "2020-05-15",
        "last_sold_price": 450000,
        "price": 500000,
        "property_size": 3000,
        "rent_price": 2500,
        "tax_value": 480000,
        "tax_year": 2022,
        "year_built": 1998,
        "rentzestimate_amount": 2400,
        "rentzestimate_last_updated": "2023-09-01",
        "zestimate_amount": 510000,
        "zestimate_last_updated": "2023-09-01",
        "street": "123 Main St",
        "city": "Seattle",
        "state": "WA",
        "zipcode": "98101"
    }

    post:

    Create a new Zillow listing with the provided property details.

    post_request:

    {
        "zillow_id": 12345678,
        "link": "https://www.zillow.com/homedetails/12345678_zpid/",
        "area_unit": "SqFt",
        "bathrooms": 2.5,
        "bedrooms": 4,
        "home_size": 2500,
        "home_type": "SingleFamily",
        "last_sold_date": "2020-05-15",
        "last_sold_price": 450000,
        "price": 500000,
        "property_size": 3000,
        "rent_price": 2500,
        "tax_value": 480000,
        "tax_year": 2022,
        "year_built": 1998,
        "rentzestimate_amount": 2400,
        "rentzestimate_last_updated": "2023-09-01",
        "zestimate_amount": 510000,
        "zestimate_last_updated": "2023-09-01",
        "street": "123 Main St",
        "city": "Seattle",
        "state": "WA",
        "zipcode": "98101"
    }

    post_response:

    HTTP 201 Created

    {
        "id": "1db4e4ae-b969-42e7-85e9-bdf56c9c4d87",
        "zillow_id": 12345678,
        "link": "https://www.zillow.com/homedetails/12345678_zpid/",
        "area_unit": "SqFt",
        "bathrooms": 2.5,
        "bedrooms": 4,
        "home_size": 2500,
        "home_type": "SingleFamily",
        "last_sold_date": "2020-05-15",
        "last_sold_price": 450000,
        "price": 500000,
        "property_size": 3000,
        "rent_price": 2500,
        "tax_value": 480000,
        "tax_year": 2022,
        "year_built": 1998,
        "rentzestimate_amount": 2400,
        "rentzestimate_last_updated": "2023-09-01",
        "zestimate_amount": 510000,
        "zestimate_last_updated": "2023-09-01",
        "street": "123 Main St",
        "city": "Seattle",
        "state": "WA",
        "zipcode": "98101"
    }

    '''

    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.ZillowListingSerializer
    queryset = models.ZillowListing.objects.all()
