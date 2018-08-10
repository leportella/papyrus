import json

import pytest

from .factories import FeatureFactory, UserFactory


@pytest.fixture
def data():
    return {
        'description': 'This is a description',
        'priority': 1,
        'product_area': '4',
        'target_date': '2018-08-08',
        'title': 'Title',
    }


@pytest.mark.django_db
def test_list_features(client):
    FeatureFactory()
    response = client.get('/features/')
    content = json.loads(response.content)
    assert len(content['objects']) == 1


@pytest.mark.django_db
def test_create_feature(client, data):
    user = UserFactory()
    data.update({'client': user.id})
    response = client.post('/features/', json.dumps(data),
                           content_type="application/json")
    content = json.loads(response.content)
    assert content['priority'] == 1
    assert content['feature_title'] == 'Title'
    assert content['client_name'] == user.email


@pytest.mark.django_db
def test_create_feature_reprioritizing(client, data):
    user = UserFactory()
    data.update({'client': user.id})
    feature = FeatureFactory(priority=1, client=user)

    response = client.post('/features/', json.dumps(data),
                           content_type="application/json")
    content = json.loads(response.content)
    assert content['priority'] == 1
    assert content['feature_title'] == 'Title'
    assert content['client_name'] == user.email

    feature.refresh_from_db()
    assert feature.priority == 2
