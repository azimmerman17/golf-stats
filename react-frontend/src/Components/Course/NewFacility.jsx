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
import Messages from '../Home/Messages';

const NewFacility = ({}) => {
  const BASE_URL = import.meta.env.VITE_BACKEND_URL
  const [validated, setValidated] = useState(false)
  const [message, setMessage] = useState([])
  const [newFacility, setNewFacility] = useState({
    name: null,
    classification: 'D',
    hole_count: 18,
    established: new Date().getFullYear(),
    website: null,
    address: null,
    city: null,
    state: null,
    country: 'USA',
    geo_lat: null,
    geo_lon: null,
  })
  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Courses', path: '/course', active: true},
    {name: 'New Facility', page: 'new facility', active: false}
  ]

  const formItems = [
    {name: 'Name', type: 'text', placeholder: 'Facility Name', required: true, formText: null, validationText: 'Please enter a name for the facility', field: 'name'},
    {name: 'Classification', type: 'select', placeholder: 'Facility Classification', required: true, formText: null, field: 'classification', list: CourseClassList},
    {name: 'Hole Count', type: 'number', placeholder: newFacility.holeCount, required: true, formText: null, field: 'hole_count', min: 0, max: 999},
    {name: 'Established', type: 'number', placeholder:  newFacility.established, required: false, formText: null, field: 'established', min: 1400, max: new Date().getFullYear()},
    {name: 'Website', type: 'text', placeholder: 'Facility Website', required: false, formText: null, field: 'website'},
    {name: 'Address', type: 'text', placeholder: 'Facility Address', required: false, formText: null, field: 'address'},
    {name: 'City', type: 'text', placeholder: 'Facility City', required: true, formText: null, validationText: 'Please enter the city where the facility is located', field: 'city'},
    {name: 'State', type: 'typeahead', placeholder: 'Facility State', required: false, formText: null, validationText: 'Please enter the state where the facility is located', field: 'state', list: StateList, disabled: newFacility.country !=='USA'},
    {name: 'Country', type: 'typeahead', placeholder:  newFacility.country, required: true, formText: null, field: 'country', list: CountryList},
    {name: 'Coordinates Latitude', type: 'text', placeholder: 'Facility Coordinates Latitude', required: false, formText: null, validationText: 'Invalid Latitudinal Value',  field: 'geo_lat', min: -90, max: 90},
    {name: 'Coordinates Longitude', type: 'text', placeholder: 'Facility Coordinates Longitude', required: false, formText: null, validationText: 'Invalid Longitudinal Value', field: 'geo_lon', min:-180, max: -180}
  ]

  const displayMessages = message.map((m, i) => {
    const { color, text } = m

    return <Messages color={color} text={text} key={`message-${i}`}/>
  })

  const displayForm = formItems.map(item => {
    const { name } = item

    return <FormGroupTriage formData={item} formObj={newFacility} control='newFacility' setFormObj={setNewFacility} validated={validated} key={`new-facility-form-${name}`} />
  })

  const handleSubmit = async (e) => {
    e.preventDefault()
   const form = e.currentTarget
    if (form.checkValidity() === false) {
      e.preventDefault()
      e.stopPropagation()
    }

    // reset state
    setValidated(true)
    setMessage([])

    // // validate form
    // formItems.forEach(item => {
    //   const handleInvalid = (text) => {
    //     setValidated(false)
    //     console.log(text)
    //     setMessage([...message, text])
    //     console.log(message)
    //   }

    //   const { required, field, name, validationText } = item
    //   if (required === true && !newFacility[field]) handleInvalid(validationText)
    //   if (name === 'State' && newFacility.country === 'USA' && !newFacility[field]) handleInvalid(validationText)
    //   if (name === 'Coordinates Latitude' && newFacility[field] && (!Number(newFacility[field]) || Number(newFacility[field]) > 90 || Number(newFacility[field]) < -90))  handleInvalid(validationText)
    //   if (name === 'Coordinates Longitude' && newFacility[field] && (!Number(newFacility[field]) || Number(newFacility[field]) > 180 || Number(newFacility[field]) < -180)) handleInvalid(validationText)
    // })

    // submit the form -- 
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'mode': 'cors',
      },
      body: JSON.stringify(newFacility)
    }

    let response = await fetch(BASE_URL + 'facility/', options)
    const data = await response.json()

    if (response.status === 200) {
      setCurrentUser(data.user)
      setMessage([])
      setCurrentPage('facility')
    } else {
      setMessage({color: 'danger', text: data.message})
    }
  }


  return (
    <Container fluid>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row>
        {message.length > 0 ? {displayMessages} : null}
      </Row>
      <Row>
        <h5 className='text-center'>Add New Facility</h5>
        <Form className='mb-3'   validated={validated} onSubmit={handleSubmit}>
          {displayForm}
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </Row>
    </Container>
  )
}

export default NewFacility