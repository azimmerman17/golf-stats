import { Marker } from 'react-leaflet/Marker'
import { Popup } from 'react-leaflet/Popup'

const MapMarker = ({ position, popup }) => {

  return (
    <Marker position={position}>
      {popup ? (
        <Popup>
          {popup}
        </Popup>
      ) : null}
    </Marker>
  )

}

export default MapMarker