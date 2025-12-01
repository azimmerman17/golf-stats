import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import GetClassification from '../../../Functions/GetClassification'
import InfoDisplay from '../../../Functions/InfoDisplay'

const FacilityHomeTab = ({ facility, season, course }) => {
  const { city, classification, established, hole_count, state, country } = facility
  const { end_date, start_date, year_round } = season

  const dataList = [
    {data: established, label: 'ESTABLISHED'},
    {data: GetClassification(classification), label: 'CLASSIFICATION'},
    {data: course, label: 'COURSE COUNT'},
    {data: hole_count, label: 'HOLE COUNT'},
    {data: `${city}${state ? `, ${state}` : ''}`, label: 'LOCATION'},
    {data: country, label: 'COUNTRY'},
    {data: year_round ? 'YEAR ROUND' : `${start_date} - ${end_date}`, label: 'HANDICAP SEASON'},
  ]

  const display = dataList.map(item => {
    const { data, label }= item

    return (
      <Col xs={6} key={`Facility-Home-Tab-${label}`}>
        <InfoDisplay data={data} label={label} />
      </Col>
    )
  })

  return (
    <Container fluid>
      <Row>
        {display}
      </Row>
    </Container>
  )
}

export default FacilityHomeTab