import json

import pytest

from factories import FeatureFactory


@pytest.fixture
def customer():
    return FeatureFactory()


@pytest.mark.django_db
def test_testcase(client, customer):
    response = client.get('/features/')
    content = json.loads(response.content)
    assert len(content['objects']) == 1
