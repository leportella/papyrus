import datetime
import factory
from factory import fuzzy

from django.contrib.auth.models import User

from feature.models import Feature


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda o: '{}.{}'.format(
        o.first_name.lower(), o.last_name.lower()))
    email = factory.LazyAttribute(lambda o: '{}.{}@example.com'.format(
        o.first_name.lower(), o.last_name.lower()))


class FeatureFactory(factory.DjangoModelFactory):
    class Meta:
        model = Feature

    client = factory.SubFactory(UserFactory)
    description = fuzzy.FuzzyText(length=100)
    priority = fuzzy.FuzzyInteger(1, 100)
    product_area = fuzzy.FuzzyChoice(['1', '2', '3', '4'])
    status = fuzzy.FuzzyChoice(['1', '2', '3', '4'])
    target_date = datetime.date(2008, 1, 1)
    title = fuzzy.FuzzyText(length=50)
