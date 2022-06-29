from django.urls import include, path
from rest_framework import routers

from api.views import (CommentViewSet, FollowViewSet, GroupViewSet,
                       PostViewSet, UserViewSet)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register(r'follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
