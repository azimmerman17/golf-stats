import { useMap } from 'react-leaflet/hooks'

const SetView = ({ loc, zoom }) => {
  const map = useMap()
  map.setView(loc,zoom);
}

export default SetView