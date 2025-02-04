from django.shortcuts import render
from rest_framework import viewsets

from . import serializers
from . import models


class HouseViewSet(viewsets.ModelViewSet):
    '''
    Creating, reading, deleting updating and replacing of a House.
    '''

    serializer_class = serializers.HouseSerializer
    queryset = models.House.objects.all()
