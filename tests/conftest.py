import pytest
from rest_framework.test import APIClient
from tests.test_users.factories import ProprietarioFactory, UserFactory


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def simple_user():
    return UserFactory()


@pytest.fixture
def proprietario_user():
    return ProprietarioFactory()


@pytest.fixture
def simple_user_buider():
    return UserFactory.build()


@pytest.fixture
def proprietario_user_buider():
    return ProprietarioFactory.build()
