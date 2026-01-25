import { useContext } from 'react';
import { useSearchParams } from 'react-router-dom';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image';
import ListGroup from 'react-bootstrap/ListGroup';

import { CurrentPage } from '../../Contexts/CurrentPageContext'
import { CurrentFacility } from '../../Contexts/CurrentFacilityContext';

const CourseCard = ({ item }) => {
  const [searchParams, setSearchParams] = useSearchParams()
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const { currentFacility, setCurrentFacility } = useContext(CurrentFacility)

  const { facility } = item
  const { handle, name, facility_id, city, country, state } = facility
  
  const handleClick = (id) => {
    setSearchParams({ facility_id: id });
    setCurrentPage('facility')
    console.log(currentFacility)
  }
  
  return (
    <ListGroup.Item className='px-1' onClick={e => handleClick(facility_id)}>
      <Container fluid className='px-0'>
        <Row className='px-0'>
          <Col xs='2' className='me-1 ms-0 p-1 text-center'>
            {handle ? <Image src={`https://logos.bluegolf.com/${handle}/profile.png`} alt={`${name} Logo`} style={{ maxWidth: '100px'}} className='m-auto'/> : null}
          </Col>
          <Col xs='9'>
            <h6>{name}</h6>
            <p className='mb-0 text-end text-secondary small-text'>{city}{state ? ` ${state}` : '' }, {country}</p>
          </Col>
        </Row>
      </Container>
    </ListGroup.Item>

)

}

export default CourseCard