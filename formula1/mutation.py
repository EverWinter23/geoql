from base64 import b64encode as b64E

import graphene
from graphene.relay.node import to_global_id

from graphene_gis.scalars import LineStringScalar
from django.contrib.gis.geos import GEOSGeometry

from formula1.models import F1Track
from formula1.query import F1TrackType


class CreateF1TrackMutationWithWKT(graphene.Mutation):
    id = graphene.String()
    name = graphene.String()
    length = graphene.Int()
    geometry = LineStringScalar()

    class Arguments:
        name = graphene.String()
        length = graphene.Int()
        geometry = graphene.String()

    def mutate(self, info, name, length, geometry):
        track = F1Track(name=name, length=length, geometry=geometry)
        track.save()

        return CreateF1TrackMutationWithWKT(
            id=to_global_id(F1TrackType.__name__, track.id),
            name=track.name,
            length=track.length,
            geometry=track.geometry,
        )


class CreateF1TrackMutationWithGeoJSON(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    length = graphene.Int()
    geometry = LineStringScalar()

    class Arguments:
        name = graphene.String()
        length = graphene.Int()
        geometry = graphene.JSONString()

    def mutate(self, info, name, length, geometry):
        track = F1Track(name=name, length=length, geometry=GEOSGeometry(f"{geometry}"))
        track.save()

        return CreateF1TrackMutationWithGeoJSON(
            id=to_global_id(F1TrackType.__name__, track.id),
            name=track.name,
            length=track.length,
            geometry=track.geometry,
        )
