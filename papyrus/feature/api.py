from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import Feature


class FeatureResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'priority': 'priority',
        'client_name': 'client.email',
        'feature_title': 'title',
    })

    def list(self):
        return Feature.objects.all()
