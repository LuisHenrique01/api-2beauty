from cgi import print_form
import pytest
from django.forms.models import model_to_dict
from users.api.serializers import ProprietarioSerializer, UserChangePasswordSerializer, UserCreateSerializer, UserDetailSerializer

pytestmark = pytest.mark.unit


class TestUserSerializers:

    def test_user_create_serializer_model(self, simple_user_buider):
        serializer = UserCreateSerializer(simple_user_buider)
        assert serializer.data

    @pytest.mark.django_db
    def test_user_create_serializer_data(self, simple_user_buider):
        serializer = UserCreateSerializer(
            data=model_to_dict(simple_user_buider)
        )
        assert serializer.is_valid()
        assert serializer.errors == {}

    def test_user_detail_serializer_model(self, simple_user_buider):
        expected_data = {
            'email': simple_user_buider.email,
            'first_name': simple_user_buider.first_name,
            'id': simple_user_buider.id,
            'username': simple_user_buider.username
        }
        serializer = UserDetailSerializer(simple_user_buider)
        assert serializer.data == expected_data

    @pytest.mark.django_db
    def test_change_password_encrypt(self, simple_user):
        new_password_decrypt = {'password': 'LuisPass01'}
        instance_update = UserChangePasswordSerializer().update(
            simple_user, new_password_decrypt)
        assert instance_update.password != new_password_decrypt['password']

    def test_proprietario_create_serializer_model(self, proprietario_user_buider):
        serializer = ProprietarioSerializer(proprietario_user_buider)
        assert serializer.data

    @pytest.mark.django_db
    def test_proprietario_create_serializer_data(self, simple_user, proprietario_user_buider):
        proprietario_user_buider.user = simple_user
        serializer = ProprietarioSerializer(
            data=model_to_dict(proprietario_user_buider)
        )
        assert serializer.is_valid()
        assert serializer.errors == {}
