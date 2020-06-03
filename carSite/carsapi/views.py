import logging
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

logger = logging.getLogger(__name__)

from .serializers import CarsUserSerializer
from .models import (
    Profile,
    User,
)


class CarsUsersViewSet(ModelViewSet):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = CarsUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            try:
                user = User.objects.get(username=request.data.get("email"))
                profile = Profile.objects.get(user=user)
                profile.phone = request.data.get("phone")
                profile.save()
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.data.get("email"), first_name=request.data.get("name"),
                                    email=request.data.get("email"))
                Profile.objects.create_profile(user, request.data.get("phone"))
            finally:
                headers = self.get_success_headers(serializer.data)
                return Response(data=serializer.data, status=HTTP_201_CREATED, headers=headers)
        else:
            return Response(data='{detail: invalid payload}', status=HTTP_400_BAD_REQUEST)
