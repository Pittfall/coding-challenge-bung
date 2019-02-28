from rest_framework import serializers

from . import models


class HouseSerializer(serializers.ModelSerializer):
    """A serializer for House model."""

    last_sold_date = serializers.DateField(
        allow_null=True, input_formats=["%m/%d/%Y"])
    rentzestimate_last_updated = serializers.DateField(
        allow_null=True, input_formats=["%d/%m/%Y"])
    zestimate_last_updated = serializers.DateField(
        allow_null=True, input_formats=["%m/%d/%Y"])

    class Meta:
        model = models.House
        fields = '__all__'
