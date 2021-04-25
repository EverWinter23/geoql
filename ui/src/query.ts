export const DEFAULT_QUERY = `
  mutation TrackMutationWithWKT {
    createTrack(
      name:"Bahrain",
      length:500,
      geometry: "SRID=4326;POLYGON ((-80 25, -65 18, -64 32, -80 25))"
    ) {
      id
      name
      length,
      geometry
    }
  }
  
  mutation TrackMutationWithJSON {
    createTrackWithGeojson(
      name:"Bahrain 2.0",
      length:500,
      geometry: "{\\"type\\":\\"Polygon\\",\\"coordinates\\":[[[-80,25],[-65,18],[-64,32],[-80,25]]]}"
    ) {
      id
      name
      length,
      geometry
    }
  }
  
  query GetTracks{
    allTracks {
      edges {
        node {
          id
          name
          length,
          geometry
        }
      }
    }
  }
`;


