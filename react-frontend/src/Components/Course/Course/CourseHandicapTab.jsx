import { useState } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import InputGroup from 'react-bootstrap/InputGroup'
import Form from 'react-bootstrap/Form'

import Dropdowns from '../../Home/Dropdowns'
import InfoDisplay from '../../../Functions/InfoDisplay'
import CalculateCourseHandicap from '../../../Functions/CalculateCourseHandicap'

const CourseHandicapTab = ({tees, currentTee, setCurrentTee}) => {
  const [gender, setGender] = useState('M')
  const [index, setIndex] = useState('0.0')

  // Build Dropdowns
  let teeDropdown = []
  tees.forEach(t => {teeDropdown.push({name: t.name, selected: t})})
  let genderDropdown = [
    {name: 'Male', selected: 'M'},
    {name: 'Female', selected: 'F'}
  ]

  // Get course rating data
  const { course_rating, hole_count } = currentTee
  const { M, F} = course_rating
  let rating 
  // filter by selected gender
  if (gender === 'M') rating = M
  else rating = F

  // filter by the correct hole count
  rating = rating.filter(r =>r.hole_count == hole_count)[0]
  console.log(rating)



  console.log(tees, currentTee)
  return (
     <Container fluid>
      <Row className='my-1 text-center'>
        <Col>
          <Form.Control placeholder={index} className='text-center w-25 m-auto' onChange={e => setIndex(e.target.value)}/>
          <p className='text-muted mb-0'><small>HANDICAP INDEX</small></p>
        </Col>
        <Col>
          <Dropdowns items={teeDropdown} color={'white'} id={'tee-handicap-dropdown'} align='start' current={currentTee ? currentTee.name : teesSorted[0].name} setCurrent={setCurrentTee} />
          <p className='text-muted mb-0'><small>TEE</small></p>
        </Col>
        <Col>
          <Dropdowns items={genderDropdown} color={'white'} id={'gender-handicap-dropdown'} align='start' current={gender} setCurrent={setGender} />
          <p className='text-muted mb-0'><small>GENDER</small></p>
        </Col>
      </Row>
      <hr className='text-danger' />
      {rating ? (
        <>
          <Row className='my-1 text-center'>
            <Col>
              <InfoDisplay data={rating.course_rating} label={'Course Rating'}  /> 
            </Col>
            <Col>
              <InfoDisplay data={rating.slope} label={'Slope'}  />
            </Col>
            <Col>
              <InfoDisplay data={rating.par} label={'Par'}  />
            </Col>
          </Row>
          <hr className='text-danger' />
          <Row className='my-1 text-center'>
            <h4 className='text-center'>{CalculateCourseHandicap(index, rating.course_rating, rating.slope, rating.par )}</h4>
            <p className='text-muted mb-0'><small>COURSE HANDICAP</small></p>
          </Row>
        </>
      ) : (
        <Row className='my-1 text-center'>
          <p className='fs-5'>No course ratings defined for this tee and gender combination</p>
        </Row>
      )}
    </Container>
  )
}

export default CourseHandicapTab