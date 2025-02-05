import pytest

from django.urls import reverse
from rest_framework import status
from model_bakery import baker

def test_list_zillow_listing_url_ok():
    target_url = '/api/listing/'
    name = 'zillowlisting-list'
    assert reverse(name) == target_url

def test_detail_zillow_listing_url_ok():
    target_url = '/api/listing/1/'
    name = 'zillowlisting-detail'
    assert reverse(name, args=[1]) == target_url


@pytest.mark.django_db
@pytest.mark.parametrize('method', ['PUT', 'PATCH', 'DELETE'])
def test_zillow_listing_view_set__methods_not_allowed(method, api_client):
    url = reverse('zillowlisting-list')

    api_client.force_authenticate(user=baker.make('auth.User'))
    response = api_client.generic(method, url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
@pytest.mark.parametrize(
    'is_authenticated, expected_status',
    [
        (True, status.HTTP_200_OK),
        (False, status.HTTP_401_UNAUTHORIZED),
    ]
)
def test_get_zillow_listing_authentication(api_client, is_authenticated, expected_status):
    listing = baker.make('challenge_api.ZillowListing')
    url = reverse('zillowlisting-detail', args=[listing.id])

    if is_authenticated:
        api_client.force_authenticate(user=baker.make('auth.User'))

    response = api_client.get(url)

    assert response.status_code == expected_status


@pytest.mark.django_db
@pytest.mark.parametrize(
    'is_authenticated, expected_status',
    [
        (True, status.HTTP_201_CREATED),
        (False, status.HTTP_401_UNAUTHORIZED),
    ]
)
def test_post_zillow_listing_authentication(api_client, is_authenticated, expected_status):
    url = reverse('zillowlisting-list')

    payload = {
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

    if is_authenticated:
        api_client.force_authenticate(user=baker.make('auth.User'))

    response = api_client.post(url, data=payload)

    assert response.status_code == expected_status
