from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from blog_drf.yasg import yasg_urlpatterns as yasg_url


api_urlpatterns = [
    path('comments/', include('apps.comments.urls')),
    path('favorites/', include('apps.favorites.urls')),
    path('likes/', include('apps.likes.urls')),
    path('posts/', include('apps.posts.urls')),
    path('users/', include('apps.users.urls')),

    # authorization
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # drf_yasg
    path('', include(yasg_url)),

    # api
    path('', include(api_urlpatterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
