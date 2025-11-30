import { useContext } from 'react';
import { useSearchParams } from 'react-router-dom';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { CurrentPage } from '../../../Contexts/CurrentPageContext'
import { CurrentFacility } from '../../../Contexts/CurrentFacilityContext';

import Breadcrumbs from '../../Home/BreadCrumbs';
import FacilityHeader from './FacilityHeader';

const FacilityHome = ({}) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const { currentFacility, setCurrentFacility } = useContext(CurrentFacility)

  if (!currentFacility) return 'Loading...'
  const { course, facility, season } = currentFacility
  const { name } = facility
  
  console.log(course, facility, season)

  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Courses', path: '/course', active: true},
    {name: name.length > 25 ? `${name.substring(0, 24).trim()}...` : name, page: 'facility', active: false},
  ]
  
  return (
    <Container fluid className='p-1'>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row>
        <FacilityHeader facility={facility} season={season}/>
      </Row>
    </Container>
  )
}

export default FacilityHome