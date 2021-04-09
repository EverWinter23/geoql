import uuid
from django.contrib.gis.db import models


class F1Track(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(max_length=128, null=False)
    length = models.PositiveIntegerField(null=False)
    geometry = models.PolygonField(null=False)
