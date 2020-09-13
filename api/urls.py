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
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
