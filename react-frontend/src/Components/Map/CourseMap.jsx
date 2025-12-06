import { MapContainer } from 'react-leaflet/MapContainer'
import { TileLayer } from 'react-leaflet/TileLayer'

import MapPolyLine from './Utilities/MapPolyline'
import MapMarker from './Utilities/MapMarker'

const CourseMap = ({ gps }) => {
  const mapLayer = {
    layerName: 'Satellite', 
    url:`https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}`, 
    attribution: `&copy; <a href=https://www.google.com/maps/place/ target='_black'>View on Google Maps</a>`, 
    subdomains: ['mt0','mt1','mt2','mt3']
  }

  // calculate course center
  let cLat = 0
  let cLon = 0
  let minZoom = 20

  gps.forEach(hole => {
    const { tee_lat, tee_lon, zoom } = hole
    if (minZoom > zoom) minZoom = zoom
    cLat += tee_lat
    cLon += tee_lon

  })

  const center = [cLat / gps.length, cLon / gps.length]

  const courseMarkings = gps.map(item => {
    const { dl2_lat, dl2_lon, dl_lat, dl_lon, green_center_lat, green_center_lon, tee_lat, tee_lon, hole_geo_id, number } = item

    const points = [
      {lat: tee_lat, lon: tee_lon, marker: 'Tee'},
      {lat: dl_lat, lon: dl_lon, marker: 'Dogleg'},
      {lat: dl2_lat, lon: dl2_lon, marker: 'Dogleg 2'},
      {lat: green_center_lat, lon: green_center_lon, marker: 'Green'},
    ]

    let polyPoints = []
    points.forEach((item) => {
      const { lat, lon } = item
      if (lat) polyPoints.push([lat, lon])
    })
    
    return (
      <div key={`Course-map-hole-${number}`}>
        <MapPolyLine points={polyPoints} id={hole_geo_id} color={'red'} />
        <MapMarker position={[tee_lat, tee_lon]} popup={`Hole ${number}`} />
      </div>
    )
  })

  return (
    <MapContainer center={center} zoom={minZoom - 1} scrollWheelZoom={false} id='course-map' className='mx-auto my-2'> 
      <TileLayer
        url={mapLayer.url}
        maxZoom= {20}
        attribution={mapLayer.attribution}
        subdomains={mapLayer.subdomains}
      />
      {courseMarkings}
    </MapContainer>
  )
}

export default CourseMap