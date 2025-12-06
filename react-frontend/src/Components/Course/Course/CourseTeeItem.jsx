import Accordion from 'react-bootstrap/Accordion'
import Container from 'react-bootstrap/Container'
import Col from 'react-bootstrap/esm/Col'
import Row from 'react-bootstrap/Row'
import InfoDisplay from '../../../Functions/InfoDisplay'

const CourseTeeItem = ({ tee, i }) => {
  const { course_id, course_rating, hole_count, meters, name, tee_id, yards } = tee
  const { M, F } = course_rating
  
  // hard coding distance units - will be apart of user settings
  let units = 'yards'

  let teeData = [
    {data: yards, label: 'YARDS'},
    {data: meters, label: 'METERS'},
    {data: hole_count, label: 'TOTAL HOLES'}
  ]

  // add only the Full course Ratings 
  let menRating = []
  let ladiesRating = []

  const buildRatingArr = (r) => {
    const { par, course_rating, slope } = r

    return [
      {data: par, label: 'PAR'},
      {data: course_rating, label: 'COURSE RATING'},
      {data: slope, label: 'SLOPE'}
    ]
  }
  
  // Men's Rating - if exists
  if (M.length > 0) menRating = buildRatingArr(M.filter(rating => rating.hole_count === hole_count)[0])

  // Ladies's Rating - if exists
  if (F.length > 0) ladiesRating = buildRatingArr(F.filter(rating => rating.hole_count === hole_count)[0])

  const dataDisplay = teeData.map(item => {
    const { data, label } = item
    if ((label === 'YARDS' || label === 'METERS') && units.toUpperCase() != label) return null
    return (
      <Col key={`data-display-tee-${tee_id}-${label}`} >
        <InfoDisplay data={data} label={label}  />
      </Col>
    )
  })

  const menDisplay = menRating.map(item => {
    const { data, label } = item
    return (
      <Col key={`men-rating-display-tee-${tee_id}-${label}`} >
        <InfoDisplay data={data} label={label}  />
      </Col>
    )
  })

  const ladiesDisplay = ladiesRating.map(item => {
    const { data, label } = item
    return (
      <Col key={`ladies-rating-display-tee-${tee_id}-${label}`} >
        <InfoDisplay data={data} label={label}  />
      </Col>
    )
  })

  return (
    <Accordion.Item eventKey={tee_id}>
      <Accordion.Header>
        <h6>{name}</h6>
      </Accordion.Header>
      <Accordion.Body>
        <Container fluid>
          <Row>
            {dataDisplay}
          </Row>
          {menRating.length > 0 ? <hr className='text-danger' /> : null}
          {menRating.length > 0 ? (
            <Row>
              <p className='text-center mb-1'>Men's Ratings</p>
              {menDisplay}
            </Row>
            
          ): null}
          {ladiesRating.length > 0 ? <hr className='text-danger' /> : null}
          {ladiesRating.length > 0 ? (
            <Row>
              <p className='text-center mb-1'>Ladies' Ratings</p>
              {ladiesDisplay}
            </Row>
          ): null}
        </Container>
      </Accordion.Body>
    </Accordion.Item>
  )
}

export default CourseTeeItem