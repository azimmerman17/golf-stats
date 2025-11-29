import { useContext } from 'react'
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { CourseList } from '../../Contexts/CourseListContext';


import Breadcrumbs from '../Home/BreadCrumbs'
import DisplayCards from '../Home/DisplayCards';
import CourseCard from './CourseCard';

const CourseHome = ({}) => {
  const { courseList, setCourseList} = useContext(CourseList)


  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Courses', path: '/course', active: false}
  ]

  const pageCards = [
    {title: 'Home', icon: 'Home', path: '/', space: true},
    {title: 'New Course', icon: 'Course Plus', page: 'new', space: true}
  ]

  const courseNames = courseList.map(item => {
    const { facility_id } = item.facility
    
    return (
      <CourseCard item={item}  key={`CourseCard-${facility_id}`}/>
    )
  })

  const navCards = pageCards.map(card => {
    const { title, icon, path, page, space} = card
    
    return (
      <Col className='mx-auto p-1' key={`CourseNavCard-${title}`}>
        <DisplayCards title={title} icon={icon} page={page} path={path} space={space} />
      </Col>
    )
  })

  return (
     <Container fluid>
      <Row>
          <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row>
        <Card border='danger' className='border border-5 px-2'>
          <ListGroup variant='flush'>
            {courseNames} 
          </ListGroup>
        </Card>
      </Row>
      <Row>
        {navCards}
      </Row>
    </Container>
  )
}



export default CourseHome