import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/esm/Col'
import InfoDisplay from '../../../Functions/InfoDisplay'

import ConvertUnits from '../../../Functions/ConvertUnits'

const CourseHoleDetails = ({ currentHole, greenDepth }) => {
  if (!currentHole) return <p>Loading...</p>
  const { female, male, meters, number, yards } = currentHole

  // hard coding distance units - will be apart of user settings
  let units = 'yards'

  const detailArr = [
    {data: greenDepth, label: 'GREEN DEPTH'},
    {data: meters, label: 'METERS'},
    {data: yards, label: 'YARDS'}
  ]

  const showdetails = detailArr.map(item => {
    let { data, label } = item

    if (units === 'yards' && label === 'METERS' || (units === 'meters' && label === 'YARDS')) return null
    if (units === 'meters' && label === 'GREEN DEPTH') data = ConvertUnits(data, 'yards', 'meters')

    return (
      <Col key={`hole-${number}-${label}`}>
        <InfoDisplay data={data} label={label} />
      </Col>
    )
  })

  const genderDetails = (gender) => {
    const { par, si } = gender
    const genderArry = [
      {data: par, label: 'PAR'},
      {data: si, label: 'STROKE INDEX'},
    ]

    const genderDisplay = genderArry.map(item => {
      const { data, label } = item

      return (
        <Col key={`hole-${number}-${label}`}>
          <InfoDisplay data={data} label={label} />
        </Col>
      )
    })

    return genderDisplay
  }


  return (
    <Container fluid>
      <Row>
        {showdetails}
      </Row>
      {male ? <hr className='text-danger' /> : null}
      {male ? (
        <Row>
          <p className='text-center mb-1'>Men's Details</p>
          {genderDetails(male)}
        </Row>
      ) : null}
      {female ? <hr className='text-danger' /> : null}
      {female ? (
        <Row>
          <p className='text-center mb-1'>Ladies' Details</p>
          {genderDetails(female)}
        </Row>
      ) : null}
    </Container>
  )
}

export default CourseHoleDetails