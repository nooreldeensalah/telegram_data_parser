from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomAuthToken, user_logout, CredentialViewSet

router = DefaultRouter()
router.register(r'credentials', CredentialViewSet)

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('', include(router.urls)),
]
