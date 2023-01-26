from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.favorites.serializers import FavoriteSerializers
from apps.posts.serializers import PostSerializer

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'image',
            'bio',
            'phone_number',
            'create_at',
            'password',
        )

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'image',
            'bio',
            'phone_number',
        )


class UserListSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(read_only=True, many=True)
    user_favorite = FavoriteSerializers(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'image',
            'bio',
            'email',
            'phone_number',
            'user_posts',
            'user_favorite'
        )
