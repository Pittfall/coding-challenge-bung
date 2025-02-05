import pytest
from rest_framework.test import APIClient

@pytest.fixture()
def api_client():
    '''Rest Framework's client class which extends Django's'''
    return APIClient()