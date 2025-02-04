from rest_framework import serializers

from . import models


class HouseSerializer(serializers.ModelSerializer):
    '''
    A serializer for House model.
    '''

    class Meta:
        model = models.House
        fields = '__all__'
