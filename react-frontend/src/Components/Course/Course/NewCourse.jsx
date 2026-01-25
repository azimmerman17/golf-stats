import { useSearchParams } from 'react-router-dom'
import { useContext, useState } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'

import { CurrentFacility } from '../../../Contexts/CurrentFacilityContext';
import { CurrentPage } from '../../../Contexts/CurrentPageContext'


import Breadcrumbs from '../../Home/BreadCrumbs'
import Messages from '../../Home/Messages'
import FormGroupTriage from '../../Forms/FormGroupTriage'

const NewCourse = ({}) => {
  const BASE_URL = import.meta.env.VITE_BACKEND_URL
  const [searchParams, setSearchParams] = useSearchParams()
  const { currentFacility, setCurrentFacility } = useContext(CurrentFacility)
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const [validated, setValidated] = useState(false)
  const [message, setMessage] = useState([])
  const [course, setCourse] = useState({
    course_handle: null,
    established: new Date().getFullYear(),
    architect: null,
    hole_count: 18,
    GHIN: "",
    gps_data:""
  })

  if (!currentFacility) return 'Loading...'

  const facilityId = searchParams.get('facility_id')
  const { facility, season } = currentFacility

  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Courses', path: '/course', active: true},
    {name: facility.name.length > 25 ? `${facility.name.substring(0, 24).trim()}...` : facility.name, page: 'facility', active: true},
    {name: 'New Course' , page: 'newCourse', active: false},
  ]

  const formItems = [
    {name: 'Course Handle', type: 'text', placeholder: 'Bluegolf Handle', required: false, formText: null, field: 'course_handle'},
    {name: 'Established', type: 'number', placeholder: course.established, required: false, formText: null, field: 'established', min: 1400, max: new Date().getFullYear()},
    {name: 'Hole Count', type: 'number', placeholder: course.hole_count, required: false, formText: null, field: 'hole_count', min: 0, max: 999},
    {name: 'Architect', type: 'text', placeholder: 'Course Architect', required: false, formText: null, field: 'architect'},
    {name: 'GHIN Data', type: 'text', placeholder: 'Course data from the Course Rating Database', required: false, formText: null, field: 'GHIN'},
    {name: 'Hole GPS Data', type: 'text', placeholder: 'Hole by Hole GPS Data', required: false, formText: null, field: 'gps_data'},
  ]

  const displayForm = formItems.map(item => {
    const { name } = item

    return <FormGroupTriage formData={item} formObj={course} control='newcourse' setFormObj={setCourse} validated={validated} key={`new-course-form-${name}`} />
  })

  const handleSubmit = async (e) => {
    e.preventDefault()

    const form = e.currentTarget
    if (form.checkValidity() === false) {
      e.preventDefault()
      e.stopPropagation()
    }

    setValidated(true)

    
    const {course_handle, established, architect, hole_count, GHIN, gps_data } = course
    
    const formData = {
      User: {
        course_handle,
        established: Number(established),
        architect,
        hole_count: Number(hole_count)
      },
      GHIN: JSON.parse(GHIN),
      gps_data: JSON.parse(gps_data)
    }
    
    
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'mode': 'cors',
      },
      body: JSON.stringify(formData)
    }

    let response = await fetch(BASE_URL + `facility/${facilityId}`, options)
    const data = await response.json()

    if (response.status === 200) {
      let g = JSON.parse(GHIN)
      setSearchParams({ facility_id: g.Facility.FacilityId });
      setCurrentPage('facility')
    } else {
      setMessage({color: 'danger', text: data.message})
    }

  }

  const displayMessages = message.map((m, i) => {
    const { color, text } = m

    return <Messages color={color} text={text} key={`message-${i}`}/>
  })


  return (
    <Container fluid>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row>
        {message.length > 0 ? {displayMessages} : null}
      </Row>
      <Row>
        <h5 className='text-center'>Add New Course</h5>
        <Form className='mb-3' validated={validated} onSubmit={handleSubmit}>
          {displayForm}
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </Row>

    </Container>
  )
}

export default NewCourse