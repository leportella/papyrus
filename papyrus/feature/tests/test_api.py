import json

import pytest

from .factories import FeatureFactory, UserFactory


def data(user):
    return {
        'description': 'This is a description',
        'priority': 1,
        'product_area': '4',
        'target_date': '2018-08-08',
        'title': 'new_priority_1',
        'client': user.id,
    }

def post(client, url, body):
    response = client.post(url, body, content_type="application/json")
    return json.loads(response.content)

@pytest.fixture
def user():
    user = UserFactory()
    FeatureFactory(title='priority_1', client=user, priority=1)
    FeatureFactory(title='priority_2', client=user, priority=2)
    return user


@pytest.mark.django_db
def test_list_features(client, user):
    response = client.get('/features/')
    content = json.loads(response.content)
    assert len(content['objects']) == 2


@pytest.mark.django_db
def test_create_feature_reprioritizing(client, user):
    body = json.dumps(data(user))
    content = post(client, '/features/', body)

    assert content['priority'] == 1
    assert content['feature_title'] == 'new_priority_1'
    assert content['client_name'] == user.email

    for feature in user.features.all():
        if feature.title == 'new_priority_1':
            assert feature.priority == 1
        if feature.title == 'priority_1':
            assert feature.priority == 2
        if feature.title == 'priority_2':
            assert feature.priority == 3


@pytest.mark.django_db
@pytest.mark.parametrize('attribute', [
    'description',
    'priority',
    'product_area',
    'target_date',
    'client',
    'title'
])
def test_create_feature_errors(client, user, attribute):
    body = data(user)
    body.pop(attribute)
    content = post(client, '/features/', body)
    assert content['error'][attribute] ==  ['This field is required.']
