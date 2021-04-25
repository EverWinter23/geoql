import uuid
from django.contrib.gis.db import models


class F1Track(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False,
    )

    name = models.CharField(max_length=128, null=False)
    length = models.PositiveIntegerField(null=False)
    geometry = models.LineStringField(null=False)
