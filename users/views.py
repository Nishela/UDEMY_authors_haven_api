from collections import defaultdict

from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, permissions

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    action_permissions = defaultdict(
        lambda: (permissions.IsAuthenticated,),
        {
            "list": (permissions.IsAdminUser,)
        }
    )

    def get_permissions(self):
        return [permission() for permission in self.action_permissions[self.action]]
