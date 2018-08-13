import json

import pytest

from django.contrib.auth.models import User

from feature.models import Feature
from .factories import FeatureFactory


@pytest.fixture
def body():
    return {
        'description': 'This is a description',
        'priority': 1,
        'product_area': '4',
        'target_date': '2018-08-08',
        'title': 'new_priority_1',
        'client': 'A',
    }


def post(client, url, body):
    response = client.post(url, json.dumps(body),
                           content_type="application/json")
    return json.loads(response.content)


@pytest.fixture
def user():
    user = User.objects.create_user(username='john.snow', password='targaryen')
    FeatureFactory(title='priority_1', client='A', priority=1)
    FeatureFactory(title='priority_2', client='A', priority=2)
    return user


def authenticate(client):
    client.login(username='john.snow', password='targaryen')


@pytest.mark.django_db
def test_list_features(client, user):
    authenticate(client)
    response = client.get('/api/features/')
    content = json.loads(response.content)
    assert len(content['objects']) == 2


@pytest.mark.django_db
def test_create_feature_reprioritizing(client, user, body):
    authenticate(client)
    content = post(client, '/api/features/', body)

    assert content['priority'] == 1
    assert content['title'] == 'new_priority_1'
    assert content['client'] == 'John Snow'

    assert Feature.objects.get(title='new_priority_1').priority == 1
    assert Feature.objects.get(title='priority_1').priority == 2
    assert Feature.objects.get(title='priority_2').priority == 3


@pytest.mark.django_db
@pytest.mark.parametrize('attribute', [
    'description',
    'priority',
    'product_area',
    'target_date',
    'client',
    'title'
])
def test_create_feature_errors(client, user, body, attribute):
    authenticate(client)
    body.pop(attribute)
    content = post(client, '/api/features/', body)
    assert content['error'][attribute] == ['This field is required.']
