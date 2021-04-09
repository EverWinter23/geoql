import graphene
from graphene.relay import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from graphene_gis.converter import gis_converter  # noqa

from formula1.models import F1Track


class F1TrackType(DjangoObjectType):
    class Meta:
        model = F1Track
        fields = ["name", "length", "geometry"]
        filter_fields = ["id"]
        interfaces = [Node]


class Formula1Query(graphene.ObjectType):
    track = Node.Field(F1TrackType)
    all_tracks = DjangoFilterConnectionField(F1TrackType)
