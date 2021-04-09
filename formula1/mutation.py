import graphene

from graphene_gis.scalars import PolygonScalar
from django.contrib.gis.geos import GEOSGeometry

from formula1.models import F1Track


class CreateF1TrackMutationWithWKT(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    length = graphene.Int()
    geometry = PolygonScalar()

    class Arguments:
        name = graphene.String()
        length = graphene.Int()
        geometry = graphene.String()

    def mutate(self, info, name, length, geometry):
        track = F1Track(name=name, length=length, geometry=geometry)
        track.save()

        return CreateF1TrackMutationWithWKT(
            id=track.id,
            name=track.name,
            length=track.length,
            geometry=track.geometry,
        )


class CreateF1TrackMutationWithGeoJSON(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    length = graphene.Int()
    geometry = PolygonScalar()

    class Arguments:
        name = graphene.String()
        length = graphene.Int()
        geometry = graphene.JSONString()

    def mutate(self, info, name, length, geometry):
        track = F1Track(name=name, length=length, geometry=GEOSGeometry(f"{geometry}"))
        track.save()

        return CreateF1TrackMutationWithGeoJSON(
            id=track.id,
            name=track.name,
            length=track.length,
            geometry=track.geometry,
        )
