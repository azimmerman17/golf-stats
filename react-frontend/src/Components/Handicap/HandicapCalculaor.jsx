import { useState } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/esm/Col'
import Form from 'react-bootstrap/Form'
import FloatingLabel from 'react-bootstrap/FloatingLabel'

import CalculateCourseHandicap from '../../Functions/CalculateCourseHandicap'
import InfoDisplay from '../../Functions/InfoDisplay'

const HandicapCalculator = ({current}) => {
  const { hi_value } = current
  const [courseData, setCourseData] = useState(
    {
      index: hi_value,
      slope: 113,
      rating: 72.0,
      par: 72
    }
  )
  console.log(courseData)
  const { index, slope, rating, par } = courseData

  const DisplayInput = (value, label, field) => {
    const handleChange = (v, f) => {
      switch (f) {
        case 'index': 
          setCourseData({...courseData, index: v})
          break
        case 'slope': 
          setCourseData({...courseData, slope: v})
          break
        case 'rating': 
          setCourseData({...courseData, rating: v})
          break
        case 'par': 
          setCourseData({...courseData, par: v})
          break
      }
    }

    return (
      <FloatingLabel
        controlId={`calc_${label}`}
        label={label}
        className="mb-3"
      >
        <Form.Control type="text" placeholder={value} value={value} onChange={e => handleChange(e.target.value, field)}/>
      </FloatingLabel>
    )
  }

  return (
    <Container fluid className='m-0 p-0 w-100 h-100 border border-danger rounded border-2 shadow-lg'>
      <Row className='my-2'>
        <h4 className='text-center text-bottom m-0'>Course Handicap Calculator</h4>
      </Row>
      <hr className='mx-2 my-0'/>
      {hi_value > 54 ? (
        <p className='text-center m-2 py-4'>Unable to calcuate a Course Handicap without a valid index</p>
      ) : (
        <>
          <Row className='text-center p-1'>
            <Col md={6} className='text-center'>{DisplayInput(index, 'HANDICAP INDEX', 'index')}</Col>
            <Col md={6} className='text-center'>{DisplayInput(rating, 'COURSE RATING', 'rating')}</Col>
            <Col md={6} className='text-center'>{DisplayInput(slope, 'SLOPE RATING', 'slope')}</Col>
            <Col md={6} className='text-center'>{DisplayInput(par, 'PAR', 'par')}</Col>
          </Row>
          <Row className='my-2'>
            <Col><InfoDisplay data={CalculateCourseHandicap(index, rating, slope, par)} label={'COURSE HANDICAP'} /></Col>
          </Row>
        </>
      )}
    </Container>


)
}

export default HandicapCalculator
// {/* <Form.Label htmlFor="inputPassword5">Password</Form.Label>
//       <Form.Control
//         type="password"
//         id="inputPassword5"
//         aria-describedby="passwordHelpBlock"
//       />
//       <Form.Text id="passwordHelpBlock" muted>
//         Your password must be 8-20 characters long, contain letters and numbers,
//         and must not contain spaces, special characters, or emoji.
//       </Form.Text> */}