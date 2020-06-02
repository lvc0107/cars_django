from rest_framework import serializers

from .models import CarsUsers


class CarsUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarsUsers
        fields = ('id', 'created_at',)
