from rest_framework import viewsets

from .serializers import CarsUserSerializer
from .models import CarsUsers


class CarsUsersViewSet(viewsets.ModelViewSet):
    queryset = CarsUsers.objects.all().order_by('id')
    serializer_class = CarsUserSerializer
