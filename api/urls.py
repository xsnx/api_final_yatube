from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from api.views import APIPostDetail, APICommentDetail, APIFollow, APIGroup

router = DefaultRouter()
router.register(r'posts', APIPostDetail)
router.register(r'posts/(?P<post_id>\d+)/comments', APICommentDetail,
                basename='APIComment')
router.register(r'follow', APIFollow,
                basename='Follow')
router.register(r'group', APIGroup,
                basename='Group')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
