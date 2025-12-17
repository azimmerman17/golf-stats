import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import Breadcrumbs from '../Home/BreadCrumbs'
import FormGroupTriage from '../Forms/FormGroupTriage';
import { useState } from 'react';
import CountryList from '../../Assests/CountryList';
import StateList from '../../Assests/StateList';
import CourseClassList from '../../Assests/CourseClassList';

const NewFacility = ({}) => {
  const [newFacility, setNewFacility] = useState({
    name: null,
    classification: 'O',
    holeCount: 18,
    established: new Date().getFullYear(),
    website: null,
    address: null,
    city: null,
    state: null,
    country: 'USA',
    lat: null,
    lon: null,
  })
  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Courses', path: '/course', active: true},
    {name: 'New Facility', page: 'new facility', active: false}
  ]
  console.log(newFacility)
  const formItems = [
    {name: 'Name', type: 'text', placeholder: 'Facility Name', required: true, formText: null, field: 'name'},
    {name: 'Classification', type: 'select', placeholder: 'Facility Classification', required: true, formText: null, field: 'classification', list: CourseClassList},
    {name: 'Hole Count', type: 'number', placeholder: newFacility.holeCount, required: true, formText: null, field: 'holeCount', min: 0, max: 999},
    {name: 'Established', type: 'number', placeholder:  newFacility.established, required: false, formText: null, field: 'established', min: 1400, max: new Date().getFullYear()},
    {name: 'Website', type: 'text', placeholder: 'Facility Website', required: false, formText: null, field: 'website'},
    {name: 'Address', type: 'text', placeholder: 'Facility Address', required: false, formText: null, field: 'address'},
    {name: 'City', type: 'text', placeholder: 'Facility City', required: true, formText: null, field: 'city'},
    {name: 'State', type: 'typeahead', placeholder: 'Facility State', required: false, formText: null, field: 'state', list: StateList, disabled: newFacility.country !=='USA'},
    {name: 'Country', type: 'typeahead', placeholder:  newFacility.country, required: true, formText: null, field: 'country', list: CountryList},
    {name: 'Coordinates Latitude', type: 'number', placeholder: 'Facility Coordinates Latitude', required: false, formText: null, field: 'lat', min: -90, max: 90},
    {name: 'Coordinates Longitude', type: 'number', placeholder: 'Facility Coordinates Longitude', required: false, formText: null, field: 'lon', min:-180, max: -180}
  ]

  const displayForm = formItems.map(item => {
    const { name } = item

    return <FormGroupTriage formData={item} formObj={newFacility} control='newFacility' setFormObj={setNewFacility}  key={`new-facility-form-${name}`} />
  })

  return (
    <Container fluid>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row>
        <h5 className='text-center'>Add New Facility</h5>
        <Form>
          {displayForm}
        </Form>
      </Row>
    </Container>
  )
}

export default NewFacility