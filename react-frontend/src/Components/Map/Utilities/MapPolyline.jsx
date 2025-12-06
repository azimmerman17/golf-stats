import { Polyline } from 'react-leaflet'

const MapPolyLine = ({ points, id , color }) => { 
  return <Polyline key={id} positions={points} color={color} />
}

export default MapPolyLine