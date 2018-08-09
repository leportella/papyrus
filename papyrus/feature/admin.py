from django.contrib import admin

from .models import Feature


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    ordering = ('-target_date',)
