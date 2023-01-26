from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django.contrib.auth import get_user_model

from apps.users.serializer import UserCreateSerializer, UserListSerializer, UserUpdateSerializer
from utils.permissions import IsUserOwner

# from utils.permissions import , IsOwner

User = get_user_model()


class UserApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['list']:
            return UserListSerializer
        elif self.action in ['update']:
            return UserUpdateSerializer
        return UserCreateSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]
        return [IsUserOwner()]
