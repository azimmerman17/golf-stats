import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import InfoDisplay from '../../../Functions/InfoDisplay'
import FacilityMap from '../../Map/FacilityMap'

const FacilityContactTab = ({ facility }) => {
  const { address, city, country, state, website, name } = facility

  const dataList = [
    {data: `${address}`, label: 'ADDRESS'},
    {data: `${city}, ${state ? state : country}`, label: 'CITY'},
    {data: <a href={`https://${website}`} target='_blank'>{website}</a>, label: 'WEBSITE'},
    {data: <a  className='text-black' href={`https://www.google.com/maps/dir/${name}+${address}`} target='_blank'>{name}</a>, label: 'GET DIRECTIONS'},
  ]

  const display = dataList.map(item => {
    const { data, label }= item

    return (
      <Col xs={12} key={`Facility-Home-Tab-${label}`}>
        <InfoDisplay data={data} label={label} />
      </Col>
    )
  })

  return (
    <Container fluid>
      <Row>
        {display}
      </Row>
      <Row>
       <FacilityMap facility={facility}/>
      </Row>
    </Container>
  )
}

export default FacilityContactTab