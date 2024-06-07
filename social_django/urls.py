from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
)
from app_social.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-image/', create_image),
    path('get-images/', get_images),
    path('get-images/<int:pk>/', update_image),
    # path('get-images/<int:pk>/', delete_image),
    path('profile/', get_profile),
    # path('get-posts/', get_posts),
    # path('create-post/', create_post),
    # path('get-likes/', get_likes),
    # path('create-like/', create_like),
    # path('get-comments/', get_comments),
    # path('create-comment/', create_comment),
    # path('get-shares/', get_shares),
    # path('create-share/', create_share),
    # path('get-reposts/', get_reposts),
    # path('create-repost/', create_repost),
    path('create-user/', create_user),
    path('token/', TokenObtainPairView.as_view()),
]

if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
