from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .api import CategoryViewSet, WatchGetList, ShoppingView

router = SimpleRouter()
router.register('category', CategoryViewSet)
router.register('watch', WatchGetList)
router.register('card', ShoppingView)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
