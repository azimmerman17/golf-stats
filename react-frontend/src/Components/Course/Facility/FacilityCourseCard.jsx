import { useContext } from 'react';
import { useSearchParams } from 'react-router-dom';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image';
import ListGroup from 'react-bootstrap/ListGroup';

import { CurrentPage } from '../../../Contexts/CurrentPageContext'

const FacilityCourseCard = ({ course }) => {
  const [searchParams, setSearchParams] = useSearchParams()
  const { currentPage, setCurrentPage } = useContext(CurrentPage)

  const {architect, course_id, established, name } = course

    const handleClick = (id) => {
    setSearchParams({ facility_id: searchParams.get('facility_id'), course_id: id });
    setCurrentPage('course')
  }
  

  return (
    <ListGroup.Item className='px-1' onClick={e => handleClick(course_id)}>
      <Container fluid className='px-0'>
        <Row className='px-0'>
          <Col >
            <h6 className='ps-3'>{name}</h6>
            <p className='mb-0 text-end text-secondary small-text'>{architect}, {established}</p>
          </Col>
        </Row>
      </Container> 
    </ListGroup.Item>
  )
}

export default FacilityCourseCard