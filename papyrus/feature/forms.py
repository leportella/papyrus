from django.forms import ModelForm

from feature.models import Feature


class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        exclude = ['status']
