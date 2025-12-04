import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'
import GetFlag from '../../../Functions/GetFlag'
import TranslateCountryCode from '../../../Functions/TranslateCountryCode'
import InfoDisplay from '../../../Functions/InfoDisplay'

const CourseHeader = ({ course, facility, season }) => {

  const {established, architect, course_id, facility_id, handle,hole_count, name } = course
  const { city, state, country } = facility

  return (
    <Container fluid className='border border-3 border-danger rounded p-1 shadow-lg'>
      <Row>
        <Image src={`https://logos.bluegolf.com/${handle}/profile.png`} alt={`${name} Logo`} style={{ maxWidth: '100px'}} className='m-auto'/>
      </Row>
      <Row>
         <h4 className='mx-auto mb-0 text-center align-text-bottom'>{facility.name}</h4>
         {facility.name == name ? null : <h4 className='mx-auto mb-0 text-center align-text-bottom'>{name}</h4>}
         <p className=' text-center text-secondary small-text'>{city}{state ? ` ${state}` : '' }, {country}</p>
      </Row>
      <Row> 
        <Col className='text-start'>
          <InfoDisplay data={architect} label='ARCHITECT' />
        </Col>
        <Col className='text-end'>
          <InfoDisplay data={established} label='ESTABLISHED' />
        </Col>
      </Row>
    </Container>  
  )
}

export default CourseHeader