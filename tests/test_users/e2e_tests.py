import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from .factories import ProprietarioFactory, UserFactory

pytestmark = pytest.mark.django_db


class TestProprietarioEndpoints:

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def test_create_user(self, api_client):
        user = {'username': 'luis', 'first_name': 'luis',
                'email': 'luis@gmail.com', 'password': '#SUPERsenha09'}
        response = api_client().post(
            reverse('user-create'),
            data=user,
            format='json'
        )
        self.token = dict(response.json()).get('access')

        assert response.status_code == 201
        assert 'access' in list(dict(response.json()).keys())
        assert 'refresh' in list(dict(response.json()).keys())
