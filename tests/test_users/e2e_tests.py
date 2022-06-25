import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestProprietarioEndpoints:

    def test_create_user(self, api_client):
        user = {'username': 'luis', 'first_name': 'luis',
                'email': 'luis@gmail.com', 'password': '#SUPERsenha09'}
        response = api_client().post(
            reverse('user-create'),
            data=user,
            format='json'
        )
        assert response.status_code == 201
        assert 'access' in list(dict(response.json()).keys())
        assert 'refresh' in list(dict(response.json()).keys())

    def test_get_user_unauthorized(self, api_client):
        response = api_client().get(reverse('get-user'))
        assert response.status_code == 401

    def test_get_user(self, api_client, simple_user):
        client = api_client()
        client.force_authenticate(simple_user)
        expected_dict = {
            'id': simple_user.id,
            'username': simple_user.username,
            'first_name': simple_user.first_name,
            'email': simple_user.email,
        }
        response = client.get(reverse('get-user'))
        assert response.status_code == 200
        assert response.json() != simple_user.__dict__
        assert response.json() == expected_dict

    def test_create_proprietario(self, api_client, simple_user):
        client = api_client()
        client.force_authenticate(simple_user)
        data = {
            "cpf": "789.456.123-01",
            "data_nascimento": "2002-01-20",
            "telefone": "(89) 99461-9853"
        }
        response = client.post(
            reverse('proprietario-create'),
            data=data,
            format='json'
        )
        print(response.json())
        assert response.status_code == 201

    def test_get_proprietario(self, api_client, proprietario_user):
        client = api_client()
        client.force_authenticate(proprietario_user.user)
        expected_dict_keys = ["id", "cpf", "data_nascimento",
                              "telefone", "data_cadastro", "user"]
        response = client.get(reverse('get-proprietario'))
        assert response.status_code == 200
        assert list(dict(response.json())) == expected_dict_keys

    # def test_user_change_password(self):
