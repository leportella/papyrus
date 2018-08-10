# Generated by Django 2.1 on 2018-08-10 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to=settings.AUTH_USER_MODEL),
        ),
    ]
