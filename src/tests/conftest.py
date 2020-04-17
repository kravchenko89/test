import pytest

from django.urls import reverse
from pytest_django.fixtures import _django_db_fixture_helper

from rest_framework.test import APIClient

from account.models import User


@pytest.fixture(scope='session', autouse=True)
def db_session(request, django_db_setup, django_db_blocker):

    if 'django_db_reset_sequences' in request.funcargnames:
        request.getfixturevalue('django_db_reset_sequences')
    if 'transactional_db' in request.funcargnames \
            or 'live_server' in request.funcargnames:
        request.getfixturevalue('transactional_db')
    else:
        _django_db_fixture_helper(request, django_db_blocker, transactional=False)


@pytest.fixture(scope='session')
def api_client():
    client = APIClient()  # LEGB

    def login():
        url = reverse('account:login')
        response = client.post(
            url, data={'username': 'admin@admin.com', 'password': 12345},
            format='json',
        )

        assert response.status_code == 200

    client.login = login

    yield client
