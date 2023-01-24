from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.PhoneValidates import phone_regex


class User(AbstractUser):
    username = models.CharField(
        verbose_name='username',
        max_length=12,
        unique=True
    )
    image = models.ImageField(
        upload_to='user_images/',
        verbose_name='image',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        verbose_name='phone_number',
        validators=[phone_regex],
        max_length=17,
        unique=True
    )
    bio = models.TextField(
        verbose_name='bio',
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='create_at'
    )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'Nickname: {self.username}'
    