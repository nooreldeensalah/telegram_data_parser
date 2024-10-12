from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CredentialsListView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', TokenRefreshView.as_view(), name='token_refresh'),
    path('credentials/', CredentialsListView.as_view(), name='credentials_list'),
]
