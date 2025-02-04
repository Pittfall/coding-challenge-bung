from rest_framework import serializers

from . import models


class ZillowListingSerializer(serializers.ModelSerializer):
    '''
    A serializer for ZillowListing model.
    '''

    class Meta:
        model = models.ZillowListing
        fields = '__all__'
