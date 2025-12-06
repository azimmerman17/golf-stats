import { MapContainer } from 'react-leaflet/MapContainer'
import { Marker } from 'react-leaflet/Marker'
import { Popup } from 'react-leaflet/Popup'
import { LayersControl } from 'react-leaflet/LayersControl'

import MapLayerArr from './Utilities/MapLayerArr'
import MapLayers from './Utilities/MapLayers'
import MapMarker from './Utilities/MapMarker'

const FacilityMap = ({ facility }) => {
  const { name, geo_lat, geo_lon } = facility

  const mapLayers = MapLayerArr.map(layer => {
    const { layerName } = layer

    return <MapLayers layer= {layer} key={`Facility-Map-${layerName}`} />
  })
 
  return (
    <MapContainer center={[geo_lat, geo_lon]} zoom={15} scrollWheelZoom={false} id='contact-map' className='mx-auto my-2'> 
      <LayersControl>
        {mapLayers}
      </LayersControl>
      <MapMarker position={[geo_lat, geo_lon]} popup={name} />
    </MapContainer>
  )
}


export default FacilityMap