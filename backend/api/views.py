from rest_framework import viewsets
from .models import Credentials
from .serializers import CredentialsSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

class CredentialsFilter(filters.FilterSet):
    application = filters.CharFilter(field_name="application", lookup_expr='icontains')
    username = filters.CharFilter(field_name="username", lookup_expr='icontains')
    url = filters.CharFilter(field_name="url", lookup_expr='icontains')

    class Meta:
        model = Credentials
        fields = ['application', 'username', 'url']

class CredentialsViewSet(viewsets.ModelViewSet):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CredentialsFilter
