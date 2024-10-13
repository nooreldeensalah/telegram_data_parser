from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import logout

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'email': token.user.email
        })

@api_view(['POST'])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({"message": "Successfully logged out."})


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Credential
from .serializers import CredentialSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

class CredentialsFilter(filters.FilterSet):
    application = filters.CharFilter(field_name="application", lookup_expr='icontains')
    username = filters.CharFilter(field_name="username", lookup_expr='icontains')
    url = filters.CharFilter(field_name="url", lookup_expr='icontains')

    class Meta:
        model = Credential
        fields = ['application', 'username', 'url']

class CredentialViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CredentialsFilter
