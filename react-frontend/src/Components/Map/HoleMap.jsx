import { MapContainer } from 'react-leaflet/MapContainer'
import { useMap } from "react-leaflet/hooks"
import { Marker } from 'react-leaflet/Marker'
import { Popup } from 'react-leaflet/Popup'
import { TileLayer } from 'react-leaflet/TileLayer'


import SetView from './Utilities/SetMapView'
import GetIcon from '../../Functions/GetIcon'
import MapPolyLine from './Utilities/MapPolyline'
import MapMarker from './Utilities/MapMarker'

const HoleMap = ({ mapData }) => { 
  if (!mapData) return 'Loading...'

  const { dl2_lat, dl2_lon, dl_lat, dl_lon, green_center_lat, green_center_lon, tee_lat, tee_lon, zoom, hole_geo_id, number } = mapData
  
  const mapLayer = {
    layerName: 'Satellite', 
    url:`https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}`, 
    attribution: `&copy; <a href=https://www.google.com/maps/place/ target='_black'>View on Google Maps</a>`, 
    subdomains: ['mt0','mt1','mt2','mt3']
  }

  const points = [
    {lat: tee_lat, lon: tee_lon, marker: 'Tee'},
    {lat: dl_lat, lon: dl_lon, marker: 'Dogleg'},
    {lat: dl2_lat, lon: dl2_lon, marker: 'Dogleg 2'},
    {lat: green_center_lat, lon: green_center_lon, marker: 'Green'},
  ]

  let count = 0
  let cLat = 0
  let cLon = 0
  let polyPoints = []
  points.forEach((item) => {
    const { lat, lon } = item
    if (lat) {
      cLat += lat
      cLon += lon
      count +=1
      polyPoints.push([lat, lon])
    }
  })

  const center = [cLat / count , cLon / count]

  return (
    <MapContainer center={center} zoom={zoom} scrollWheelZoom={false} id='hole-map' className='mx-auto my-2'> 
       <TileLayer
          url={mapLayer.url}
          maxZoom= {20}
          attribution={mapLayer.attribution}
          subdomains={mapLayer.subdomains}
            />
      <SetView loc={center} zoom={zoom}/>
      <MapPolyLine points={polyPoints} id={hole_geo_id} color={'red'} />
      <MapMarker position={[tee_lat, tee_lon]} popup={`Hole ${number}`} />
    </MapContainer>


  )
}

export default HoleMap