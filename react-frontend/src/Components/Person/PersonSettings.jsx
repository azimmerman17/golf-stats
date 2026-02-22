import Container from 'react-bootstrap/Container'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'

import InfoDisplay from '../../Functions/InfoDisplay'
import TranslateUnitName from '../../Functions/TranslateUnitName'

const PersonSettings = ({ person }) => {
    const { units_alt, units_distance, units_height, units_speed, units_temp, units_weight } = person

  const dataList = [
    {data: TranslateUnitName(units_alt, 'Altitue Units'), label: 'Altitue Units'},
    {data: TranslateUnitName(units_distance, 'Distance Units'), label: 'Distance Units'},
    {data: TranslateUnitName(units_speed, 'Speed Units'), label: 'Speed Units'},
    {data: TranslateUnitName(units_temp, 'Temperature Units'), label: 'Temperature Units'},
    {data: TranslateUnitName(units_weight, 'Weight Units'), label: 'Weight Units'},
    {data: TranslateUnitName(units_height, 'Height Units'), label: 'Height Units'},
  ]

  const display = dataList.map(item => {
    const { data, label }= item

    return (
      <Col xs={6} key={`Person-Bio-Tab-${label}`}>
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

export default PersonSettings
