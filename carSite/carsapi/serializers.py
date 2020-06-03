from rest_framework import serializers

from .models import Profile


class CarsUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'created_at',)

