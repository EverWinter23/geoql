import graphene

from formula1.query import Formula1Query
from formula1.mutation import (
    CreateF1TrackMutationWithWKT,
    CreateF1TrackMutationWithGeoJSON,
)


class Query(Formula1Query):
    greeting = graphene.JSONString()

    def resolve_greeting(root, info):
        return "Hello, World!"


class Mutation(graphene.ObjectType):
    create_track = CreateF1TrackMutationWithWKT.Field()
    create_track_with_geojson = CreateF1TrackMutationWithGeoJSON.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
