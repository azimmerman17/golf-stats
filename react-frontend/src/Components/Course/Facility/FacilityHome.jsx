import { useContext, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Nav from 'react-bootstrap/Nav';

import { CurrentPage } from '../../../Contexts/CurrentPageContext'
import { CurrentFacility } from '../../../Contexts/CurrentFacilityContext';

import Breadcrumbs from '../../Home/BreadCrumbs';
import FacilityHeader from './FacilityHeader';
import FacilityHomeTab from './FacilityHomeTab';
import FacilityContactTab from './FacilityContactTab';
import FacilityCourseTab from './FacilityCourseTab';

const FacilityHome = ({}) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const { currentFacility, setCurrentFacility } = useContext(CurrentFacility)
  const [facilityTab, setFacilityTab] = useState('Home')

  if (!currentFacility) return 'Loading...'
  const { course, facility, season } = currentFacility
  const { name } = facility
  
  console.log(course, facility, season)

  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Courses', path: '/course', active: true},
    {name: name.length > 25 ? `${name.substring(0, 24).trim()}...` : name, page: 'facility', active: false},
  ]

  const tabs = [
    'Home',
    'Courses',
    'Contact'
  ]

const tabLinks = tabs.map(tab => {
    return (
      <Nav.Item key={`facility-navtab-${tab}`}>
          <Nav.Link className={`bg-danger${facilityTab === tab ? ' text-white border-black border-2 fw-bold' :'-subtle text-black border-bottom'} rounded-top`}  onClick={e => setFacilityTab(tab)}>{tab}</Nav.Link>
      </Nav.Item>
    )
  })

  const tabView = (tab) => {
    switch (tab) {
      case 'Home':
        return <FacilityHomeTab facility={facility} season={season} course={course.length}/>
      case 'Courses':
        return <FacilityCourseTab course_list={course} />    
      case 'Contact':
        return <FacilityContactTab facility={facility} />
    }
  }
  
  return (
    <Container fluid className='p-1'>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row className='mb-2'>
        <FacilityHeader facility={facility} season={season} />
      </Row>
      <Row className='border border-danger border-3 rounded shadow-lg mb-3'>
        <Nav justify variant='tabs' className='border-bottom border-black border-3 p-1' defaultActiveKey='Home' activeKey='Home'>
          {tabLinks}
        </Nav>
        {tabView(facilityTab)}
      </Row>
    </Container>
  )
}

export default FacilityHome