import React, { useRef, useEffect, useState } from "react";

import GraphiQL from "graphiql";
import "graphiql/graphiql.min.css";
import mapboxgl from "mapbox-gl/dist/mapbox-gl-csp"
// eslint-disable-next-line import/no-webpack-loader-syntax
import MapboxWorker from "worker-loader!mapbox-gl/dist/mapbox-gl-csp-worker";

import { DEFAULT_QUERY } from "./query";
import "./App.css";

const URL = "http://localhost:8000/graphql/";
mapboxgl.workerClass = MapboxWorker;
mapboxgl.accessToken = 'pk.eyJ1Ijoic293amFueWFlbm5hbSIsImEiOiJjamk1dnRta3Uwb2FyM3FtcmRkM2h0Z2gwIn0.2Fuzb-3EnJBBgzCcWHwKfw';

function graphQLFetcher(graphQLParams: any): Object {
  return fetch(URL, {
    method: "post",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(graphQLParams),
    credentials: "omit"
  }).then(response => {
    return response.json();
  }).then(json => {
    console.log(json);
    return json;
  });
}



const Map = () => {
  const mapContainer = useRef();
  const [lng, setLng] = useState(42.9);
  const [lat, setLat] = useState(42.35);
  const [zoom, setZoom] = useState(9);
  const [features, setFeatures] = useState([]);

  useEffect(() => {
    const map = new mapboxgl.Map({
      container: mapContainer.current,
      style: "mapbox://styles/mapbox/light-v10",
      center: [lng, lat],
      zoom: zoom,
			attributionControl: false,
    });

    map.on('load', () => {
      map.addLayer({
        id: 'tracks',
        type: 'line',
        source: {
          type: 'geojson',
          data: {
            type: 'FeatureCollection',
            features: features,
          }
        },
        paint: {
          'line-color': "#000000",
          'line-width': 2,
        }
      });
    });

		map.addControl(new mapboxgl.AttributionControl(), 'top-right');
    return () => map.remove(); 
  });
 
  return (
    <div>
      <div className="map-container" ref={mapContainer} />
    </div>
  );
};

const App = () => {
  return (
    <div>
      <div className="geoql">
        <GraphiQL
          fetcher={graphQLFetcher}
          defaultQuery={DEFAULT_QUERY}
          variables={null}
        />
      </div>
      <Map />
    </div>
  )
};

export default App;
