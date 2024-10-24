from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import CredentialsViewSet

router = DefaultRouter()
router.register(r'credentials', CredentialsViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
