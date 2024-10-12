from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Credentials
from .serializers import CredentialsSerializer
from rest_framework import generics

class CredentialsListView(generics.ListAPIView):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer
