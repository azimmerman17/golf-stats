import { LayersControl } from 'react-leaflet/LayersControl'
import { TileLayer } from 'react-leaflet/TileLayer'

const MapLayers = ({ layer }) => {
  const { layerName, url, attribution, subdomains} = layer

  return (
    <LayersControl.BaseLayer name={layerName}>
      <TileLayer
        url={url}
        maxZoom= {20}
        attribution={attribution}
        subdomains={subdomains}
      />
    </LayersControl.BaseLayer>
  )
}

export default MapLayers