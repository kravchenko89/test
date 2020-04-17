import pytest

from django.template import Template
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_login(client):
    url = reverse('account:login')
    data = {'username': 'admin@admin.com', 'password': 12345}
    response = client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_sing_up(client):
    url = reverse('account:registration')
    response = client.post(url, data={'username': 'vadim@admin.com', 'first_name': 'Vadim',
                                      'last_name': 'Vadim', 'birth_date': '23.04.1999',
                                      'country': 'UA', 'email': 'vadim@admin.com',
                                      'phone': '', 'password': 123456789,
                                      'password_confirm': 123456789}, format='json')
    assert response.status_code == 200  # не понимаю почему 200


@pytest.mark.django_db
def test_sing_up_error(client):
    url = reverse('account:registration')
    response = client.post(url, data={'username': 'vadim@admin.com', 'first_name': 'Vadim',
                                      'last_name': 'njvnsknvn', 'birth_date': '23.04.1999',
                                      'country': 'UA', 'email': 'vadim@admin.com',
                                      'phone': '', 'password': 123456,
                                      'password_confirm': 123456789}, format='json')
    assert response.status_code == 200  # тоже самое

@pytest.mark.usefixtures
def test_teg(client, context):
    response = Template('<a href="http://127.0.0.1:81/admin/account/user/1>link</a>').render(context)
    assert response.status_code == 302


# docker exec -it backend pytest --cov=./src ./src --cov-config .coveragerc --cov-report html
