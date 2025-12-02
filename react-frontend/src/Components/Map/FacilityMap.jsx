import { MapContainer } from 'react-leaflet/MapContainer'
import { TileLayer } from 'react-leaflet/TileLayer'
import { Marker } from 'react-leaflet/Marker'
import { Popup } from 'react-leaflet/Popup'
import { LayersControl } from 'react-leaflet/LayersControl'

const FacilityMap = ({ facility }) => {
  const { name, facility_id, geo_lat, geo_lon } = facility

  const layers = [
    {layerName: 'OSM', url:'https://tile.openstreetmap.org/{z}/{x}/{y}.png', attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors', subdomains: []},
    // {layerName: 'Roads', url:`https://{s}.google.com/vt/lyrs=r&x={x}&y={y}&z={z}`, attribution: `&copy; <a href=https://www.google.com/maps/place/${geo_lat},${geo_lon} target='_black'>View on Google Maps</a>`, subdomains: ['mt0','mt1','mt2','mt3']},
    {layerName: 'Satellite', url:`https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}`, attribution: `&copy; <a href=https://www.google.com/maps/place/${geo_lat},${geo_lon} target='_black'>View on Google Maps</a>`, subdomains: ['mt0','mt1','mt2','mt3']},
    {layerName: 'Hybrid', url:`https://{s}.google.com/vt/lyrs=y&x={x}&y={y}&z={z}`, attribution: `&copy; <a href=https://www.google.com/maps/place/${geo_lat},${geo_lon} target='_black'>View on Google Maps</a>`, subdomains: ['mt0','mt1','mt2','mt3']},
    {layerName: 'Terrain', url:`https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}`, attribution: `&copy; <a href=https://www.google.com/maps/place/${geo_lat},${geo_lon} target='_black'>View on Google Maps</a>`, subdomains: ['mt0','mt1','mt2','mt3']},
  ]

  const mapLayers = layers.map(layer => {
    const { layerName, url, attribution, subdomains} = layer
    return (
      <LayersControl.BaseLayer name={layerName} key={`Facility-Map-${layerName}`}>
        <TileLayer
          url={url}
          maxZoom= {20}
          attribution={attribution}
          subdomains={subdomains}
        />
      </LayersControl.BaseLayer>
    )
  })

  
  return (
    <MapContainer center={[geo_lat, geo_lon]} zoom={15} scrollWheelZoom={false} id='contact-map' className='mx-auto my-2'> 
      <LayersControl>
        {mapLayers}
      </LayersControl>
     <Marker position={[geo_lat, geo_lon]} >
        <Popup>
          {name}
        </Popup>
      </Marker>
    </MapContainer>
  )
}


export default FacilityMap