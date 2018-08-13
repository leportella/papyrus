from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from django.db import transaction
from django.forms import ValidationError
from django.db.models import F

from .forms import FeatureForm
from .models import Feature


class FeatureResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'priority': 'priority',
        'client': 'get_client_display',
        'title': 'title',
        'target_date': 'target_date',
        'product_area': 'get_product_area_display',
        'description': 'description',
        'id': 'id',
    })

    # removing authentication to make it simpler
    def is_authenticated(self):
        return True

    def list(self):
        return Feature.objects.order_by('target_date').all()

    def create(self):
        form = FeatureForm(self.data)
        if not form.is_valid():
            raise ValidationError(form.errors)

        with transaction.atomic():
            Feature.objects.filter(
                client=form.cleaned_data['client'],
                priority__gte=form.cleaned_data['priority'],
            ).update(priority=F('priority')+1)
            feature = form.save()
        return feature

    def detail(self, pk):
        return Feature.objects.get(id=pk)
