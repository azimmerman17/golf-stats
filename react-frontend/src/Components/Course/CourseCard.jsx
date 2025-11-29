import { useContext } from 'react';
import { useSearchParams } from 'react-router-dom';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image';
import ListGroup from 'react-bootstrap/ListGroup';

import { CurrentPage } from '../../Contexts/CurrentPageContext'

const CourseCard = ({ item }) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const { facility } = item
  const { handle, name, facility_id, city, country, state } = facility
  
  const handleClick = (e, id) => {
    const new_facility_id = id
    // setCurrentFacility(id)
    // setCurrentPage('Facility')
    setSearchParams({ facility_id: id });
  }

  return (
    <ListGroup.Item className='px-1' onClick={e => handleClick(e, facility_id)}>
      <Container fluid className='px-0'>
        <Row className='px-0'>
          <Col xs='2' className='me-1 ms-0 p-1 text-center'>
            <Image variant='top' src={`https://logos.bluegolf.com/${handle}/profile.png`} alt={`${name} Logo`} style={{ width: '30px'}} className='mx-0'/>
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