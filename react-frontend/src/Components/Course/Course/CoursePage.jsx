import { useContext, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Nav from 'react-bootstrap/Nav';

import { CurrentPage } from '../../../Contexts/CurrentPageContext'
import { CurrentFacility } from '../../../Contexts/CurrentFacilityContext';

import Breadcrumbs from '../../Home/BreadCrumbs';
import CourseHeader from './CourseHeader';
import DisplayTabs from '../../../Functions/DisplayTabs';
import CourseTeesTab from './CourseTeesTab';
import CourseHolesTab from './CourseHolesTab';
import CourseHandicapTab from './CoursehandicapTab';

const CoursePage = ({}) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const { currentFacility, setCurrentFacility } = useContext(CurrentFacility)
  const [courseTab, setCourseTab] = useState('Tees')
  const [currentTee, setCurrentTee] = useState(null)

  if (!currentFacility) return 'Loading...'

  const { facility, season } = currentFacility
  const courseId = searchParams.get('course_id')

  const currentCourse = currentFacility.course.filter(c => c.course.course_id == courseId)[0]
  const { course, gps, tees } = currentCourse
  const { name } = course

  // sort tees by length - desending
  const teesSorted = tees.sort((a, b) =>  b.yards - a.yards)
  // set current tee if null
  if (!currentTee) setCurrentTee(teesSorted[0])

  //sort gps by hole number - ascending
  const gpsSorted = gps.sort((a, b) =>  a.number - a.number)

  // console.log(currentCourse)

  let breadcrumbName
  name == facility.name ? breadcrumbName = 'Course' : breadcrumbName = name

  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Courses', path: '/course', active: true},
    {name: facility.name.length > 25 ? `${facility.name.substring(0, 24).trim()}...` : facility.name, page: 'facility', active: true},
    {name: breadcrumbName > 25 ? `${breadcrumbName.substring(0, 24).trim()}...` : breadcrumbName, page: 'course', active: false},
  ]

  const tabs = [
    'Tees',
    'Handicap',
    'Holes'
  ]

  const viewTab = (tab) => {
    switch (tab) {
      case 'Tees':
        return <CourseTeesTab tees={teesSorted} currentTee={currentTee} setCurrentTee={setCurrentTee} />
      case 'Handicap':
        return <CourseHandicapTab tees={teesSorted} currentTee={currentTee} setCurrentTee={setCurrentTee} />
      case 'Holes':
        return <CourseHolesTab tees={teesSorted} gps={gpsSorted} currentTee={currentTee} setCurrentTee={setCurrentTee} />
    }
  }
  
  return (
    <Container fluid className='p-1'>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row>
        <CourseHeader course={course} facility={facility} season={season} />
      </Row>
      <Row className='border border-danger border-3 rounded shadow-lg my-2'>
        <DisplayTabs tabs={tabs} currentTab={courseTab} page='course' setCurrentTab= {setCourseTab} defaultKey={'Tees'} />
        {viewTab(courseTab)}
      </Row>
    </Container>
  )
}

export default  CoursePage