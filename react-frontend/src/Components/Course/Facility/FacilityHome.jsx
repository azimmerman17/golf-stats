import { useContext, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/esm/Col'
import Button from 'react-bootstrap/esm/Button'

import { CurrentPage } from '../../../Contexts/CurrentPageContext'
import { CurrentFacility } from '../../../Contexts/CurrentFacilityContext'

import Breadcrumbs from '../../Home/BreadCrumbs'
import FacilityHeader from './FacilityHeader'
import FacilityHomeTab from './FacilityHomeTab'
import FacilityContactTab from './FacilityContactTab'
import FacilityCourseTab from './FacilityCourseTab'
import DisplayTabs from '../../../Functions/DisplayTabs'

const FacilityHome = ({}) => {
  const [searchParams, setSearchParams] = useSearchParams()
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const { currentFacility, setCurrentFacility } = useContext(CurrentFacility)
  const [facilityTab, setFacilityTab] = useState('Home')
  const role = 'admin' // update to use user's role

  if (!currentFacility) return 'Loading...'
  const { course, facility, season } = currentFacility
  const { name } = facility
  

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
    <Container fluid className='p-1 mb-3'>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row className='mb-2'>
        <FacilityHeader facility={facility} season={season} />
      </Row>
      <Row className='border border-danger border-3 rounded shadow-lg mb-2'>
        <DisplayTabs tabs={tabs} currentTab={facilityTab} page='facility' setCurrentTab={setFacilityTab} defaultKey={'Home'} />
        {tabView(facilityTab)}
      </Row>
      {role === 'admin' ? (
        <Row className='mb-2'>
          <Col className='text-end'>
            <Button variant='warning' onClick={e => setCurrentPage('editFacility')}>Edit</Button>
          </Col>
        </Row>
      ) : null}
    </Container>
  )
}

export default FacilityHome