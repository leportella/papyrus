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
        'feature_title': 'title',
    })

    def is_authenticated(self):
        return self.request.user.is_authenticated

    def list(self):
        return Feature.objects.all()

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
