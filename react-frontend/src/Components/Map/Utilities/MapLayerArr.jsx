const MapLayerArr = [
    {layerName: 'OSM', url:'https://tile.openstreetmap.org/{z}/{x}/{y}.png', attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors', subdomains: []},
    // {layerName: 'Roads', url:`https://{s}.google.com/vt/lyrs=r&x={x}&y={y}&z={z}`, attribution: `&copy; <a href=https://www.google.com/maps/place/${geo_lat},${geo_lon} target='_black'>View on Google Maps</a>`, subdomains: ['mt0','mt1','mt2','mt3'], coords: true},
    {layerName: 'Satellite', url:`https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}`, attribution: `&copy; <a href=https://www.google.com/maps/place/ target='_black'>View on Google Maps</a>`, subdomains: ['mt0','mt1','mt2','mt3']},
    {layerName: 'Hybrid', url:`https://{s}.google.com/vt/lyrs=y&x={x}&y={y}&z={z}`, attribution: `&copy; <a href=https://www.google.com/maps/place/ target='_black'>View on Google Maps</a>`, subdomains: ['mt0','mt1','mt2','mt3']},
    {layerName: 'Terrain', url:`https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}`, attribution: `&copy; <a href=https://www.google.com/maps/place/ target='_black'>View on Google Maps</a>`, subdomains: ['mt0','mt1','mt2','mt3']},
]

export default MapLayerArr