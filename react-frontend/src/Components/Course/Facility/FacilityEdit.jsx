import { useContext, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Breadcrumbs from '../../Home/BreadCrumbs'

import { CurrentPage } from '../../../Contexts/CurrentPageContext'
import { CurrentFacility } from '../../../Contexts/CurrentFacilityContext'

const FacilityEdit = ({}) => {
  const BASE_URL = import.meta.env.VITE_BACKEND_URL
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const { currentFacility, setCurrentFacility } = useContext(CurrentFacility)
  const [validated, setValidated] = useState(false)
  const [message, setMessage] = useState([])
  const [edit, setEdit] = useState({})

  if (!currentFacility) return 'Loading...'
  const { course, facility, season } = currentFacility
  const { name, classification, hole_count, handle, established, website, address, city, state, country, geo_lat, geo_lon } = facility
  const { start_date, end_date, year_round } = season

  setEdit({
    name: name,
    classification: classification,
    hole_count: hole_count,
    handle: handle,
    established: established,
    website: website,
    address: address,
    city: city,
    state: state,
    country: country,
    geo_lat: geo_lat,
    geo_lon: geo_lon,
    start_date: start_date,
    end_date: end_date,
    year_round: year_round,
  })
     
  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Courses', path: '/course', active: true},
    {name: name.length > 25 ? `${name.substring(0, 24).trim()}...` : name, page: 'facility', active: true},
    {name: 'Edit Faciity', page: 'editFacility', active: false},
  ]

  // build form
  const formItems = [
    {name: 'Name', type: 'text', placeholder: edit.name, required: false, formText: null, field: 'name'},
    {name: 'Classification', type: 'select', placeholder: edit.classification, required: false, formText: null, field: 'classification', list: CourseClassList},
    {name: 'Handle', type: 'text', placeholder: edit.handle, required: false, formText: null, field: 'handle'},
    {name: 'Hole Count', type: 'number', placeholder: edit.holeCount, required: false, formText: null, field: 'hole_count', min: 0, max: 999},
    {name: 'Established', type: 'number', placeholder:  edit.established, required: false, formText: null, field: 'established', min: 1400, max: new Date().getFullYear()},
    {name: 'Website', type: 'text', placeholder: edit.website, required: false, formText: null, field: 'website'},
    {name: 'Address', type: 'text', placeholder: edit.address, required: false, formText: null, field: 'address'},
    {name: 'City', type: 'text', placeholder: edit.city, required: false, formText: null, field: 'city'},
    {name: 'State', type: 'typeahead', placeholder: edit.state, required: false, formText: null, field: 'state', list: StateList, disabled: edit.country !=='USA'},
    {name: 'Country', type: 'typeahead', placeholder:  edit.country, required: false, formText: null, field: 'country', list: CountryList},
    {name: 'Coordinates Latitude', type: 'text', placeholder: edit.geo_lat, required: false, formText: null,  field: 'geo_lat', min: -90, max: 90},
    {name: 'Coordinates Longitude', type: 'text', placeholder: edit.geo_lon, required: false, formText: null, field: 'geo_lon', min:-180, max: -180}
  ]

  // season fields
  const seasonFormItems = [
    {name: 'Start Date', type: 'text', placeholder: edit.start_date, required: false, formText: null, field: 'start_date'},
    {name: 'End Date', type: 'text', placeholder: edit.end_date, required: false, formText: null, field: 'end_date'},
    {name: 'Year Round', type: 'text', placeholder: edit.year_round, required: false, formText: null, field: 'year_round'},
  ]

  // update fields

  // submit
    // validate
    // submit
    // success - return to Facility Home
    // fail - stay

  return (
    <Container fluid>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
        <p>
          FacilityEdit
        </p>
    </Container>
  )

}

export default FacilityEdit