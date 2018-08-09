from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


AREAS_CHOICE = (
    ('1', 'Policies'),
    ('2', 'Billing'),
    ('3', 'Claims'),
    ('4', 'Reports'),
)

STATUS_CHOICE = (
    ('1', 'Done'),
    ('2', 'In progress'),
    ('3', 'Blocked'),
    ('4', 'Delayed'),
)


class Feature(models.Model):

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    priority = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    product_area = models.CharField(max_length=1, choices=AREAS_CHOICE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    target_date = models.DateField()
    title = models.CharField(max_length=300)
