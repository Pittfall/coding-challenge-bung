from django.shortcuts import render
from rest_framework import viewsets

from . import serializers
from . import models


class ZillowListingViewSet(viewsets.ModelViewSet):
    '''
    Creating, reading, deleting updating and replacing of a ZillowListing.
    '''

    serializer_class = serializers.ZillowListingSerializer
    queryset = models.ZillowListing.objects.all()
